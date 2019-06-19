# app/robo_advisor.py

# from .env file
from dotenv import load_dotenv
import os, requests, json

load_dotenv() #> loads contents of the .env file into the script's environment
# os.environ.get("ALPHAVANTAGE_API_KEY") #> This is my API KEY

## Process input

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=" + os.environ.get("ALPHAVANTAGE_API_KEY")
response = requests.get(request_url)
# print(type(response))
# print(response.status_code)
# print(response.text)
parsed_response = json.loads(response.text)

user_input = []

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
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")