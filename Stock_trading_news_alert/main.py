import asyncio
import requests
import telegram

stock_endpoint = 'https://www.alphavantage.co/query'
news_endpoint = "https://newsapi.org/v2/everything"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

TOKEN = "__TELE_BOT_TOKEN_HASH__"
STOCK_API_KEY = "__STOCK_API_KEY__"
NEWS_API_KEY = "__NEWS_API_KEY__"

s_parameters = {
    "function": "TIME_SERIES_DAILY",
    'symbol': STOCK,
    'apikey': STOCK_API_KEY
}

s_response = requests.get(stock_endpoint, params=s_parameters)
stock_data = s_response.json()

stock_data_list = [value for key, value in stock_data['Time Series (Daily)'].items()]

yesterday_close_price = float(stock_data_list[0]['4. close'])
before_yesterday_close_price = float(stock_data_list[1]['4. close'])

difference = abs(yesterday_close_price - before_yesterday_close_price)

difference_percentage = (difference * 100) / before_yesterday_close_price

if difference_percentage > 5 or difference_percentage < 5:
    n_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    n_response = requests.get(news_endpoint, params=n_parameters)
    news_data = n_response.json()['articles'][:3]
    sign = "🔺" if difference_percentage > 5 else "🔻"
    top_articles = [f"TESLA: {sign}5%\n\nHeadline: {article['title']}\nBrief: {article['description']}\nit worked kai !"
                    for article in news_data]
    bot = telegram.Bot(TOKEN)


    async def main():
        bot = telegram.Bot(TOKEN)
        async with bot:
            for message in top_articles:
                await bot.send_message(text=message, chat_id="__TELE_CHAT_ID__")


    asyncio.run(main())
