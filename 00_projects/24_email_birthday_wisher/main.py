import os
import sys
from dotenv import load_dotenv, find_dotenv
import smtplib
import pandas as pd
from datetime import datetime
import random

load_dotenv(find_dotenv())
my_email = os.getenv("my_email")
password = os.getenv("password")
recipient_email = os.getenv("recipient_email")

try:
    birthday_dates = pd.read_csv("00_projects/24_email_birthday_wisher/birthdays.csv")
    birthday_dates_list = birthday_dates.values.tolist()
except FileNotFoundError:
    print("Birthday dates file was not found")
    sys.exit()

today = (datetime.now().day, datetime.now().month)

letters = []

for textfile in os.listdir("00_projects/24_email_birthday_wisher/letter_templates"):
    with open(f"00_projects/24_email_birthday_wisher/letter_templates/{textfile}", "r") as letter:
        letters.append(letter.read())

def send_email(name, email):
    random_letter = random.choice(letters)
    random_letter = random_letter.replace("[NAME]", name)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f"Subject:Happy Birthday\n\n{random_letter}",
        )

for record in birthday_dates_list:
    birthday = (record[4], record[3])
    if birthday == today:
        name = record[0]
        email = record[1]
        send_email(name, email)

    