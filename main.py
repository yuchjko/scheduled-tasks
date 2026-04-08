# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import smtplib, random, pandas, os
import datetime as dt

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

df = pandas.read_csv("birthdays.csv")

today_month = dt.datetime.now().month
today_day = dt.datetime.now().day

for index, row in df.iterrows():
    condition_month = row["month"]
    condition_day = row["day"]
    new_name = row["name"]
    if condition_month == today_month and condition_day == today_day:

        with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt", "r") as f:
            letter_raw = f.read()
        mail_body = letter_raw.replace("[NAME]", new_name)

        with smtplib.SMTP("smtp.gmail.com") as smtp:
            smtp.starttls()
            smtp.login(my_email, my_password)
            smtp.sendmail(my_email,
                      row["email"],
                      f"Subject:Happy Birthday!\n\n{mail_body}")
