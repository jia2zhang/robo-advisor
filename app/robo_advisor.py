# app/robo_advisor.py

# from .env file
from dotenv import load_dotenv
import os, requests, json

load_dotenv() #> loads contents of the .env file into the script's environment
# os.environ.get("ALPHAVANTAGE_API_KEY") #> This is my API KEY
stock_symbol = input("Please input a stock symbol like 'MSFT', or 'DONE' if there are no more items:")

## Process input

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+stock_symbol+"&apikey=" + os.environ.get("ALPHAVANTAGE_API_KEY")
response = requests.get(request_url)
parsed_response = json.loads(response.text)
print(response)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

def to_usd(cost):
    return str("${0:,.2f}".format(cost))

tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd.keys()) # TODO: Need to make sure the dates are sorted with the latest first
latest_day = dates[0]
latest_close = tsd[latest_day]["4. close"]

# Max of all the high prices
high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[latest_day]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[latest_day]["3. low"]
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)

# user_input = []
# while True:
#     x = input("Please input a stock symbol like 'MSFT', or 'DONE' if there are no more items:")
#     if x.lower() == "done":
#         break
#     Valid_product_identifier = False
#     if ((isinstance(x, str) and x.upper() == True and len(x) == range(3,6)):
#         user_input.append(x)
#     else:
#         print("Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again.")
#         continue

## Process output

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")