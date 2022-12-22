import requests
import datetime
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os


STOCK = os.environ.get("STOCK_PRICE")
COMPANY_NAME = "Tesla Inc"
CONDITION = 0

# TWILLIO CREDENTIALS
#your accound_sid
#your auth_token


# API_KEYS FOR STOCKS AND NEWS
#your news api_key
#your api key for stocks' data

parameters_for_stocks = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": api_key

}


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


response = requests.get(
    url="https://www.alphavantage.co/query", params=parameters_for_stocks)
response.raise_for_status()
stock_daily = response.json()


today = datetime.date.today()
yesterday_date = today - datetime.timedelta(days=1)
day_before_yestr_date = today - datetime.timedelta(days=2)

# fetching the data from yesterday and day before
yesterday = stock_daily["Time Series (Daily)"][str(yesterday_date)]
day_before_yesterday = stock_daily["Time Series (Daily)"][str(
    day_before_yestr_date)]

# tapping into the closing prices from yesterday and the day before:
new_price = float(yesterday["4. close"])
old_price = float(day_before_yesterday["4. close"])

# calculating percentage change
percent_change = (new_price - old_price) / old_price * 100

# parameters for news_api:
parameters_for_news = {
    "q": "Tesla",
    "from": str(yesterday),
    "sortBy": "popularity",
    "apiKey": news_api

}


if percent_change > CONDITION:
    news_request = requests.get(
        url="https://newsapi.org/v2/everything", params=parameters_for_news)
    news_request.raise_for_status()
    fresh_news = news_request.json()
    articles = fresh_news["articles"][0:3]

    # sending an SMS
    for article in articles:
        title = article["title"]
        url = article["url"]
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=f"{STOCK} 🔺{round(percent_change, 2)}%\n{title} URL: {url}",
                from_='+your generated phone number',
                # to=os.environ.get("PHN")
                to="+phone number"
            )


elif percent_change < -CONDITION:
    news_request = requests.get(
        url="https://newsapi.org/v2/everything", params=parameters_for_news)
    news_request.raise_for_status()
    fresh_news = news_request.json()
    articles = fresh_news["articles"][0:3]

    # sending an SMS
    for article in articles:
        title = article["title"]
        url = article["url"]
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=f"{STOCK} 🔻{round(percent_change, 2)}%\n{title} URL: {url}",
                from_='+your generated phone number',
                # to=os.environ.get("PHN")
                to="+phone number"
            )


# else:
#     print("we're chillin")

# observing the percentage change

#     print("stock price increased")
# else:
#     print("stock went down")

# print(type(time_series))


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """


# def past():
#     for time_series in stock_daily["Time Series (Daily)"]:
#         date_object = datetime.datetime.strptime(time_series, '%Y-%m-%d').date()
#         if date_object == yesterday:
#             yesterday = date_object
#             return yesterday
#         if date_object == day_before_yesterday:
#             day_before_yesterday = date_object
