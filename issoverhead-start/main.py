import requests
from datetime import datetime

MY_LAT = 26.912434  # Your latitude
MY_LONG = 75.787270  # Your longitude

import smtplib

my_email = "vyas.priyanka.2601@gmail.com"
password="lxghvbivtchlxrqv"

connection = smtplib.SMTP("smtp.gmail.com",port=587)
connection.starttls()
connection.login(user=my_email,password=password)

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now >= sunset or time_now <= sunrise:
        return True


# If the ISS is close to my current position
if is_iss_overhead() and is_night():
    connection.sendmail(from_addr=my_email, to_addrs="priyankavyas2601@gmail.com",
                        msg=f"Subject:issoverhead\n\nIts dark")
    connection.close()


# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
