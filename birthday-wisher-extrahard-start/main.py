##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import pandas as pd
import datetime as dt
import os, random

birthday = pd.read_csv("birthdays.csv")
print(birthday)
now = dt.datetime.now()
today = (now.month, now.day)
print(today)
birthday_month = birthday['month'].loc[birthday.index[0]]
birthday_day = birthday["day"].loc[birthday.index[0]]
birthday_date = (birthday_month, birthday_day)
birthday_name = birthday["name"].loc[birthday.index[0]]
print(birthday_date)
print(birthday_name)
if birthday_date == today:
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as starting_letter:
        letter = starting_letter.read()
        new_letter = letter.replace("[NAME]", birthday_name)
        print(new_letter)
import smtplib

my_email = "vyas.priyanka.2601@gmail.com"
password="lxghvbivtchlxrqv"

connection = smtplib.SMTP("smtp.gmail.com",port=587)
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email, to_addrs="neerajkumarjolly25@gmail.com", msg=f"Subject:Birthday Wishes\n\n{new_letter}")
connection.close()


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
