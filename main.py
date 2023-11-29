# This app will send you a text message if it is supposed to rain within the next 12 hours.
import requests
from twilio.rest import Client

# Need your twilio account id and api auth token
# The url is for getting the weather data. The params are for the weather site's API
account_sid = "ACCNT_ID"
auth_token = "AUTH_TOKEN"
url = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "lat": 44.616650,
    "lon": 33.525368,
    "cnt": 4,
    "appid": "OWM_API_KEY"
}

# Retrieving the weather data via requests
response = requests.get(url=url, params=params)
response.raise_for_status()
weather_data = response.json()

# Pulling the weather codes and checking for any that indicate rain.
# aIf rain is detected, have twilio send a text.
will_rain = False
weather_codes = [weather_data["list"][_]["weather"][0]["id"] for _ in range(len(weather_data["list"]))]
for code in weather_codes:
    if code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="your text message",
        from_='twilio number',
        to='your_number'
    )
    print(message.status)