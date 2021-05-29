from pycoingecko import CoinGeckoAPI

COIN = "bitcoin"
CURRENCY = "usd"

def get_coingecko_price():
    cg = CoinGeckoAPI()
    price = cg.get_price(ids=COIN, vs_currencies=CURRENCY)
    print(price)

get_coingecko_price()