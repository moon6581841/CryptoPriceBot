import requests
import time

def get_crypto_price(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[symbol]['usd']
    else:
        print("Error fetching price")
        return None

def main():
    symbol = "bitcoin"  # Change to any crypto, e.g., "ethereum"
    alert_price = 30000  # Set your target price
    while True:
        price = get_crypto_price(symbol)
        if price:
            print(f"Current {symbol} price: ${price}")
            if price >= alert_price:
                print(f"Alert! {symbol} price has reached ${price}!")
                break
        time.sleep(60)  # Check price every 60 seconds

if __name__ == "__main__":
    main()
