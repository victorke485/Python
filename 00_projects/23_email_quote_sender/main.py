import pandas as pd
import smtplib
import random
import sys
import os
from dotenv import load_dotenv, find_dotenv


dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

my_email = os.getenv("my_email")
password = os.getenv("password")
recipient_email = os.getenv("recipient_email")

try:
    data = pd.read_csv("00_projects/23_birthday_wisher/quotes.txt")
except FileNotFoundError:
    print("Quotes file was not found")
    sys.exit()

data_list = data.values.tolist()
quote = "".join(random.choice(data_list))
print(quote)

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient_email,
        msg=f"Subject:Random Quote\n\n{quote}",
    )

