import smtplib
import datetime as dt
import random

MY_EMAIL = "codetest1989@gmail.com"
MY_PASSWORD = "phejxmrhaefwhcib"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("Birthday+Wisher+(Day+32)+start\Birthday Wisher (Day 32) start\quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=MY_EMAIL, 
            msg=f"Subject:Monday motivation\n\n{quote}"
        )