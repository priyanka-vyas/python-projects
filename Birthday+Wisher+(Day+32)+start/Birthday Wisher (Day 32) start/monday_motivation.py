import smtplib

my_email = "vyas.priyanka.2601@gmail.com"
password = "lxghvbivtchlxrqv"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email,to_addrs="priyankavyas2601@gmail.com",msg="Subject:Hello\n\nhello")
# connection.close()


import datetime as dt
import random

now = dt.datetime.now()
print(now.weekday())
with open("quotes.txt") as file:
    all_quotes = file.readlines()
    quote = random.choice(all_quotes)
    print(quote)

# read random line from file
# def random_line(afile):
#     line = next(afile)
#     for num, aline in enumerate(afile, 2):
#         if random.randrange(num):
#             continue
#         line = aline
#     return line


if now.weekday() == 0:
    connection.sendmail(from_addr=my_email, to_addrs="priyankavyas2601@gmail.com",
                        msg=f"Subject:Monday Motivation\n\n{quote}")
    connection.close()