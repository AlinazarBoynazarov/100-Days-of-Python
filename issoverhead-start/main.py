import requests
from datetime import datetime
import smtplib
import time

MY_LONG = -77.6283  # Your longitude
MY_LAT = 43.1283  # Your latitude


my_email = 'alinazarboynazarov24@gmail.com'
password = 'pnljzljrrllnhygg'


def is_overhead():
    while True:
        time.sleep(60)
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        # If the ISS is close to my current position
        # and it is currently dark
        uncertainty = 10
        if (int(MY_LAT) - uncertainty) <= iss_latitude <= (int(MY_LAT) + uncertainty) and (int(MY_LONG) - uncertainty) <= iss_longitude <= (int(MY_LONG) + uncertainty):
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()  # making connection secure
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs="aboynaza@u.rochester.edu",
                                    msg=f"Subject: ISS is right above you \n\n Current coordinates - longitude {iss_longitude}, latitude: {iss_latitude}")

        else:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()  # making connection secure
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs="aboynaza@u.rochester.edu",
                                    msg=f"Subject: ISS current coordinates\n\n Not close, current coordinates of ISS - latitude: {iss_latitude}, longitude: {iss_longitude}")


# Your position is within +5 or -5 degrees of the ISS position.

def nighttime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # if sunset <= time_now >= sunrise:
    #     return True


is_overhead()


# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
