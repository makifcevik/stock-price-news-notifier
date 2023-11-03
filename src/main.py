import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "KEY HERE"
NEWS_API_KEY = "KEY HERE"

ACCOUNT_SID = "REGISTER ON TWILIO"
AUTH_TOKEN = "REGISTER ON TWILIO"
FROM_NUMBER = "REGISTER ON TWILIO"
TO_NUMBER = "RECEIVER PHONE NUMBER"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

news_parameters = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
}

stock_response = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_price = stock_data_list[0]["4. close"]
before_yesterday_price = stock_data_list[1]["4. close"]
difference = float(yesterday_price) - float(before_yesterday_price)
percentage_dif = difference / float(before_yesterday_price) * 100

news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
articles = news_response.json()["articles"]
three_articles = articles[:3]

if percentage_dif < -5 or percentage_dif > 5:
    percentage_format = f"TSLA: 🔺{percentage_dif:.3f}%"
    if percentage_dif < 0:
        percentage_format = f"TSLA: 🔻{percentage_dif:.3f}%"

    formatted_articles = [f"{percentage_format}\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]

    # print(percentage_dif)
    # print(percentage_format)
    # print(formatted_articles)

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages \
            .create(
                body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                from_=FROM_NUMBER,
                to=TO_NUMBER
            )
