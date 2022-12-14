##################### Extra Hard Starting Project ######################
import csv
import smtplib
import datetime as dt
import random
import os

PLACEHOLDER = "[NAME]"


# my_email =  # put your email
# password =  # generate your password

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

folder_path = '/Users/alinazar/Desktop/Python/birthday-wisher-extrahard-start/letter_templates'
template_file = os.listdir(folder_path)


# Opening the birthdays csv file
with open("birthdays.csv") as data_file:
    reader = csv.reader(data_file)
    data = list(reader)

for row in data[1: len(data)-1]:
    if int(row[3]) == month and int(row[4]) == day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"{os.path.join(folder_path, random.choice(template_file))}") as data_file:
            reader = data_file.read()
            letter = reader.replace(PLACEHOLDER, row[0].strip())

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=row[1],
                    msg=f"Subject: Happy Birthday\n\n{letter}")
