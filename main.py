from d_gen import d_gen
from plot import plot
from dotenv import load_dotenv
import os
from api.bybit_api import BybitAPI
from strategies.smart_money_reversal import SmartMoneyReversal

# Load API credentials
load_dotenv()
api_key = os.getenv("BYBIT_API_KEY")
api_secret = os.getenv("BYBIT_API_SECRET")

# Initialize Bybit API and strategy
bybit_api = BybitAPI(api_key, api_secret)
strategy = SmartMoneyReversal()

# Main execution loop
while True:
    signals = strategy.evaluate_signals()
    for signal in signals:
        bybit_api.place_order(**signal)

if __name__ == '__main__':
    d_gen()
    plot()
    
