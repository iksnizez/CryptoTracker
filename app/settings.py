import os
from dotenv import Dotenv
dotenv = Dotenv(os.path.join(os.path.dirname(__file__), ".env"))
os.environ.update(dotenv)

MARKET_REFRESH_RATE=15
RETRY_RATE=20

BITFINEX_API_URL = os.environ.get("BITFINEX_API_URL")
BITTREX_API_URL = os.environ.get("BITTREX_API_URL")
GDAX_API_URL = os.environ.get("GDAX_API_URL")
GEMINI_API_URL = os.environ.get("GEMINI_API_URL")
KRAKEN_API_URL = os.environ.get("KRAKEN_API_URL")
POLONIEX_API_URL = os.environ.get("POLONIEX_API_URL")

LOGLEVEL = os.environ.get("TRACKER_LOG_LEVEL")
INITIAL_SLEEP = int(os.environ.get("INITIAL_SLEEP"))

ELASTICSEARCH_CONNECT_STRING = os.environ.get("ELASTICSEARCH_CONNECT_STRING")
INITIAL_INDEX_ARRAY = ['eth.gdax.ticker','eth.gemini.ticker','eth.bitfinex.ticker','eth.bittrex.ticker','eth.poloniex.ticker']
