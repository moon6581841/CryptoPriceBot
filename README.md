import requests
import time

# Set the crypto you want to monitor
CRYPTO_ID = "bitcoin"
CURRENCY = "usd"
ALERT_PRICE = 30000  # Change to your target price

def get_crypto_price():
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={CRYPTO_ID}&vs_currencies={CURRENCY}"
    response = requests.get(url)
    data = response.json()
    return data[CRYPTO_ID][CURRENCY]

while True:
    price = get_crypto_price()
    print(f"The current {CRYPTO_ID} price is {price} {CURRENCY}")

    if price >= ALERT_PRICE:
        print(f"Alert! {CRYPTO_ID} price is above {ALERT_PRICE} {CURRENCY}!")

    time.sleep(60)  # Wait for 1 minute before checking again
