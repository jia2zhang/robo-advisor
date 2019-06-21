# app/robo_advisor.py

# from .env file
from dotenv import load_dotenv
import os, requests, json, csv, datetime

load_dotenv() #> loads contents of the .env file into the script's environment
api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
# stock_symbol = input("Please input a stock symbol like 'MSFT', or 'DONE' if there are no more items:")

# 3-5 characters, alpha, capitalized (or i cap it), valid input
while True:
    stock_symbol = input("Please input a stock symbol like 'MSFT':")
    if len(stock_symbol) <3 or len(stock_symbol) >5 or stock_symbol.isalpha() == False:
        print("Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again.")
        break
    else:
        stock_symbol = stock_symbol.upper()
        request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={api_key}"
        response = requests.get(request_url)
        parsed_response = json.loads(response.text)
        # print(parsed_response)
        if "Meta Data" not in parsed_response:
            print("Sorry, couldn't find any trading data for that stock symbol.")
            continue
        # print(response.status_code)
        # print(stock_symbol)
        else: 
            ## Process input

            last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

            def to_usd(cost):
                return str("${0:,.2f}".format(cost))

            symbol = parsed_response["Meta Data"]["2. Symbol"]
            tsd = parsed_response["Time Series (Daily)"]
            dates = list(tsd.keys()) # TODO: Need to make sure the dates are sorted with the latest first
            latest_day = dates[0]
            latest_close = tsd[latest_day]["4. close"]
            request_time = ""+datetime.datetime.now().strftime("%Y-%m-%d %I:%M%p")
            # Add recommendation logic: (1 = risk neutral) so buyer will buy at a low price of 10% (of recent range) above the recent low
            risk_tolerance = float(input("Please input your risk tolerance on a scale of 1-10 (1 being risk neutral):"))
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
            # Read this for the calculation logic for the recommendation.
            risk_range = recent_high-recent_low
            bare_min = recent_low+(risk_range*risk_tolerance/10.0)
            recommend = ""
            gl = ""

            if float(latest_close) >= bare_min:
                recommend = "BUY"
                gl = "greater"
            else:
                recommend = "NO BUY"
                gl = "less"
            ## Process output
            csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices_"+symbol+".csv")

            csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
            with open(csv_file_path, "w") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames = csv_headers)
                writer.writeheader()
                # loop through each row to write each row

                for date in dates:
                    daily_prices = tsd[date]
                    writer.writerow({
                        "timestamp": date, 
                        "open": daily_prices["1. open"], 
                        "high": daily_prices["2. high"], 
                        "low": daily_prices["3. low"], 
                        "close": daily_prices["4. close"], 
                        "volume": daily_prices["5. volume"]
                    })

            print("-------------------------")
            print(f"SELECTED SYMBOL: {symbol}")
            print("-------------------------")
            print("REQUESTING STOCK MARKET DATA")
            print(f"REQUEST AT: {request_time}")
            print("-------------------------")
            print(f"LATEST DAY: {last_refreshed}")
            print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
            print(f"RECENT HIGH: {to_usd(float(recent_high))}")
            print(f"RECENT LOW: {to_usd(float(recent_low))}")
            print("-------------------------")
            print(f"RECOMMENDATION: {recommend}!")
            print(f"RECOMMENDATION REASON: Because based on your risk tolerance of {risk_tolerance}, the latest close is {gl} than {to_usd(bare_min)}")
            print("-------------------------")
            print(f"WRITING DATA TO CSV: {csv_file_path}...")
            print("-------------------------")
            print("HAPPY INVESTING!")
            print("-------------------------")
            break



