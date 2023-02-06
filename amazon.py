import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import smtplib

load_dotenv()


def get_price(soup):
    price_string = soup.find(name="span", class_="a-offscreen")
    temp = price_string.getText()
    price = float(temp[1:])
    return price


def main():
    # URL of Protein Powder
    URL = "https://www.amazon.com/Optimum-Nutrition-Standard-Protein-Chocolate/dp/B000QSNYGI/ref=sr_1_1?crid=1854AASE19ILE&keywords=gold%2Bstandard%2Bwhey%2Bprotein&nav_sdd=aps&qid=1674068204&refinements=p_n_feature_seven_browse-bin%3A6990060011&rnid=6990059011&s=hpc&sprefix=gold%2Bstandard%2Bwhey&sr=1-1-catcorr&th=1"

    # Parameters
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "lxml")

    if get_price(soup) >= 50:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # making connection secure
            connection.login(user=os.getenv('MY_EMAIL'),
                             password=os.getenv('PASSWORD'))
            connection.sendmail(from_addr=os.getenv('MY_EMAIL'), to_addrs="aboynaza@u.rochester.edu",
                                msg=f"Subject: I liek price \n\n The price is {get_price(soup)}")


main()
