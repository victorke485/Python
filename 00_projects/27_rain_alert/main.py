from dotenv import find_dotenv, load_dotenv
import os
import requests
import smtplib


load_dotenv(find_dotenv())

API_KEY = os.getenv("open_weather")
my_email = os.getenv("my_email")
password = os.getenv("password")
recipient_email = os.getenv("recipient_email")

parameters = {"appid": API_KEY, "lat": -1.292066, "lon": 36.821945, "cnt": 4}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast", params=parameters
)
response.raise_for_status()

data = response.json()

will_rain = False

for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain == True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg="Subject:Bring Umbrella\n\nIt's going to rain today. Remeber to bring an umbrella",
        )