import urllib.request
import json


def get_crypto_prices():
    url = (
        "https://api.coingecko.com/api/v3/simple/price"
        "?ids=bitcoin,ethereum,chainlink"
        "&vs_currencies=usd"
        "&include_24hr_change=true"
    )

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "SlawekInvestmentMonitor/1.0"}
        )

        with urllib.request.urlopen(request, timeout=15) as response:
            data = json.loads(response.read())

        return data

    except Exception as e:
        print(f"BŁĄD API: {e}")
        return None


print("================================")
print("SLAWEK INVESTMENT MONITOR")
print("================================")

data = get_crypto_prices()

if data:
    coins = {
        "BTC": "bitcoin",
        "ETH": "ethereum",
        "LINK": "chainlink"
    }

    for name, coin in coins.items():
        price = data[coin]["usd"]
        change = data[coin]["usd_24h_change"]

        print(f"{name}: ${price:,.2f} | 24h: {change:+.2f}%")
else:
    print("Nie udało się pobrać danych.")

print("================================")
print("KONIEC RAPORTU")
print("================================")
