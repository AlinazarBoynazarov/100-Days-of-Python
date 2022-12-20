import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# account_sid = os.environ.get("ACC_SID")

# auth_token = os.environ.get("AUTH_TOKEN")

response = requests.get(
    url="https://api.open-meteo.com/v1/forecast?latitude=43.156578&longitude=-77.608849&hourly=rain,snowfall&daily=temperature_2m_max,temperature_2m_min&temperature_unit=fahrenheit&timezone=America%2FNew_York")

response.raise_for_status()
weather_data = response.json()

time_list = list(weather_data["hourly"]["time"])
rain_list = list(weather_data["hourly"]["rain"])


will_rain = False

for i in range(len(time_list)):
    if float(rain_list[i]) > 0:
        will_rain = True


if will_rain:
    proxy_client = TwilioHttpClient(
        proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
            body="Ah, it's going to rain soon. Make sure you bring an UMBRELLA!",
            from_='+your twillio generated phone',
            # to=os.environ.get("PHN")
            to="+phone number you want to send"
        )

    print(message.status)


else:
    print("nice")
