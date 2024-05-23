import asyncio
import requests
import telegram

TOKEN = '__YOUR_TOKEN__' # after creating app from botfather , telegram
API_KEY = "__YOUR_API_KEY__" # api key to fetch weather data
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast" # endpoint

parameters = {
    'lat': "__YOUR_LATTITUDE__, # type: int
    'lon': "__YOUR_LONGITUDE__, # type: int
    'appid': API_KEY,
    'cnt': 4
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()


async def main():
    bot = telegram.Bot(TOKEN)
    async with bot:
        await bot.send_message(text='alert message', chat_id="chat_id") # your chat id from telegram use @get_id_bot in telegram (type: int)


will_rain = False
for i in range(len(data['list'])):
    condition_code = int(data['list'][i]['weather'][0]['id'])
    if condition_code < 700:
        will_rain = True

if will_rain:
    asyncio.run(main())
