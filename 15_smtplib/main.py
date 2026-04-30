import smtplib
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

my_email = os.getenv("my_email")
password = os.getenv("password")
recipient_email = os.getenv("recipient_email")

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient_email,
        msg="Subject:Hello\n\nThis is the body of the email",
    )