from service.bn.future.binance import BinanceUMFutures

class BnUMFuturesTradeListResponse:
    def __init__(self, response: list[dict]):
        self.response = response

    def get_by_symbol(self, symbol: str) -> dict:
        for r in self.response:
            if r["symbol"] == symbol:
                return r
        return None


class BnUMFuturesTrade:
    def __init__(self, binance_um_futures: BinanceUMFutures):
        self.binance_um_futures = binance_um_futures

    def get_position_inforamtion_v2(self, symbol: str) -> BnUMFuturesTradeListResponse :
        response = self.binance_um_futures.client.get_position_risk(symbol=symbol)
        return BnUMFuturesTradeListResponse(response)
    
    def query_position_inforamtion_v2(self, symbol: str) -> dict :
        response = self.binance_um_futures.client.query_order(symbol=symbol)
        return response