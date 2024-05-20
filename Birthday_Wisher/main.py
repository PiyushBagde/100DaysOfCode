import datetime as dt
import random
import smtplib

import pandas as pd

PLACEHOLDER = "[NAME]"
MY_EMAIL = "your.email@gmail.com"
PASSWORD = "yourPassword"

# 1. Update the birthdays.csv
# Done
# 2. Check if today matches a birthday in the birthdays.csv

# today's month and day
now = dt.datetime.now()
birth_day = now.day
birth_month = now.month

data = pd.read_csv('birthdays.csv')

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

if birth_month in list(data.month) and birth_day in list(data.day):
    random_letter = f"letter_{random.randint(1, 3)}.txt"

    with open(f"./letter_templates/{random_letter}") as file:
        message = file.readlines()
        birthday_person = data[data['day'] == birth_day]

        name = birthday_person['name'].to_string(index=False)
        email = birthday_person['email'].to_string(index=False)

        message[0] = message[0].replace(PLACEHOLDER, name)
        wishes = "".join(message)

# 4. Send the letter generated in step 3 to that person's email address.

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # added for security
    connection.login(user=MY_EMAIL, password=PASSWORD)  # get login here
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=email,
                        msg=f"Subject:Happy Birthday!\n\n{wishes}"
                        )
    print("Sent")
