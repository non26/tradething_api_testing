from binance.um_futures import UMFutures
import os

class BinanceUMFutures:
    def __init__(self):
        self._client = UMFutures(
            key=os.getenv("BINANCE_API_KEY"), 
            secret=os.getenv("BINANCE_API_SECRET"), 
            base_url="https://testnet.binancefuture.com" )
        
    @property
    def client(self):
        return self._client

