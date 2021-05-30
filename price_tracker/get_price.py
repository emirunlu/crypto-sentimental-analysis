from pycoingecko import CoinGeckoAPI

COIN = "bitcoin"
CURRENCY = "usd"

def get_coingecko_price():
    cg = CoinGeckoAPI()
    price = cg.get_price(ids=COIN, vs_currencies=CURRENCY)
    return price[COIN][CURRENCY]

def get_coingecko_price_history(date):
    cg = CoinGeckoAPI()
    price = cg.get_coin_history_by_id(id=COIN, date=date)
    return price["market_data"]["current_price"]["usd"]