import requests
from twilio.rest import Client

API_KEY = "__YOUR_API_KEY__"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "__YOUR_ACC_SID__"
auth_token = "__YOUR_AUTH_TOKEN__"

parameters = {
    'lat': 31.476580,
    'lon': 92.056061,
    'appid': API_KEY,
    'cnt': 4
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for i in range(len(data['list'])):
    condition_code = int(data['list'][i]['weather'][0]['id'])
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Bring Umbrella ☔",
        from_='__YOUR_TWILIO_NUMBER__',
        to='+__NUMBER_YOU_WANT_TO_ALERT__'
    )

    print(message.status)
