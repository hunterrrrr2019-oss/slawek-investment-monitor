import urllib.request
import json

def get_price(symbol):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read())

        price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
        return price

    except Exception as e:
        return f"BŁĄD: {e}"


assets = {
    "BTC": "BTC-USD",
    "ETH": "ETH-USD",
    "LINK": "LINK-USD",
    "DINO": "DNP.WA",
    "VERTIV": "VRT",
    "VISTRA": "VST",
    "MARVELL": "MRVL",
    "MICRON": "MU",
    "MP MATERIALS": "MP",
    "CAMECO": "CCJ",
    "CORNING": "GLW",
}

print("================================")
print("SLAWEK INVESTMENT MONITOR")
print("================================")

for name, symbol in assets.items():
    price = get_price(symbol)
    print(f"{name}: {price}")

print("================================")
print("KONIEC RAPORTU")
print("================================")
