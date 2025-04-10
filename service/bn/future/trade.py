from bn.binance import BinanceUMFutures

class BnUMFuturesTrade:
    def __init__(self, binance_um_futures: BinanceUMFutures):
        self.binance_um_futures = binance_um_futures

    def get_position_inforamtion_v2(self, symbol: str) -> dict :
        response = self.binance_um_futures.client.get_position_risk(symbol=symbol)
        return response
    
    def query_position_inforamtion_v2(self, symbol: str) -> dict :
        response = self.binance_um_futures.client.query_order(symbol=symbol)
        return response