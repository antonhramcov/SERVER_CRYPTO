import ccxt
from models import add_new_price
from environs import Env


env = Env()
env.read_env()
client = ccxt.bybit({
    'apiKey': env('API_KEY'),
    'secret': env('API_SECRET'),
    'enableRateLimit': True,
})

with open("symbols.txt", "r") as f:
    symbols = list(map(lambda x: x.rstrip(), f.readlines()))
prices = client.fetch_tickers(symbols)
dic1 = {}
for key, val in prices.items():
    dic1[key]=str((val['average']))
add_new_price(dic1)