import requests
from twilio.rest import Client
#Stock API
STOCK = "TCS.BSE"
COMPANY_NAME = "TATA CONSULTANCY SERVICES LTD."
FUNCTION = "TIME_SERIES_DAILY_ADJUSTED"
API_KEY = "32907DZY25MCIVJH"
STOCK_URL = "https://www.alphavantage.co/query"

# News API
NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_KEY = "22e51431dc8147aaa531eba951c4ddc0"

#Twilio API
ACC_ID = "ACf3e38966a2a6ed12bb2b6e7dd4fe7f3e"
AUTH_TOKEN = "e79b5d03c3d622d4d84215746393f45f"
TWILIO_NUMBER = "+15856011963"

stock_parameter = {
    "function": FUNCTION,
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": API_KEY,
}

news_parameter = {
    "q": "tata",
    "language":"en",
    "pageSize":3,
    "apiKey": NEWS_KEY,
}

price_response = requests.get(STOCK_URL, params=stock_parameter)
price_response.raise_for_status()
stock_data = price_response.json()

stock_price_data = [data for day,data in stock_data["Time Series (Daily)"].items()]

yesterday_close_price = stock_price_data[0]['4. close']
parso_close_price = stock_price_data[1]['4. close']

# Take 2% of previous closing price. 
delta = abs(float(yesterday_close_price) - float(parso_close_price))
check_delta = float(yesterday_close_price) - float(parso_close_price)
delta_perc = (delta / float(yesterday_close_price))*100

if delta_perc >= 2:

    news_response = requests.get(NEWS_URL,params=news_parameter) 
    news_response.raise_for_status()
    news = news_response.json()
    headlines = [item["title"] for item in news["articles"]]
    if check_delta >1:
        message = f"TCS: 🔺{round(delta_perc,1)}%\nHeadline:\n1: {headlines[0]}\n2: {headlines[1]}"
    elif check_delta <1:
        message = f"TCS: 🔻{round(delta_perc,1)}%\nHeadline:\n1: {headlines[0]}\n2: {headlines[1]}"

    client = Client(ACC_ID,AUTH_TOKEN)
    message = client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to="+917905524372")


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

