import requests, smtplib, os

END_POINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("WEATHER_API_KEY")

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

parameters = {
    "lat": 10.783634,  # Vĩ độ của bạn
    "lon": 106.6427513, # Kinh độ của bạn
    "cnt": 4,
    "appid": API_KEY
}

response = requests.get(    END_POINT, params=parameters)
# print(response.status_code)
response.raise_for_status()
data = response.json()

print(data)

def check_rain():
    will_rain = False
    for item in data["list"]:
        print(item["weather"][0]["id"])
        if item["weather"][0]["id"] < 700:
            will_rain = True
            break
    return will_rain

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as smtp:
        smtp.starttls()
        smtp.login(MY_EMAIL,MY_PASSWORD)
        smtp.sendmail(MY_EMAIL,
                      MY_EMAIL,
                      f"Subject:Rain Alert!\n\nBring an umbrella!")

if check_rain():
    send_email()






