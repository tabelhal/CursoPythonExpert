#pip install yfinance
import yfinance as yf

tickers = {
    "GOOGL": "Google",
    "AAPL": "Apple",
    "MSFT": "Microsoft",
    "META": "Meta",
    "AMZN": "Amazon"
}

eurusd = yf.Ticker("EURUSD=X").info.get("regularMarketPrice")
usd_to_eur = 1 / eurusd

for symbol, name in tickers.items():
    stock = yf.Ticker(symbol)
    info = stock.info

    price_usd = info.get("currentPrice")
    change = info.get("regularMarketChangePercent")

    if price_usd is not None and change is not None:
        price_eur = price_usd * usd_to_eur
        sign = "+" if change >= 0 else ""
        print(f"{name}: €{price_eur:.2f} ({sign}{change:.2f}%)")
    else:
        print(f"{name}: data not available")

