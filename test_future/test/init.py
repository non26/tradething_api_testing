from requests import Response
from typing import Callable      
from service.dynamodb.init.dynamodb import DynamoDB
from service.bn.future.binance import BinanceUMFutures
from service.bn.future.trade import BnUMFuturesTrade
from service.dynamodb.future.bn_future_crypto_table import BNFutureCryptoTable
from service.dynamodb.future.bn_future_history_table import BNFutureHistoryTable
from service.dynamodb.future.bn_future_opening_position_table import BNFutureOpeningPositionTable
from service.tradething.trade_future import TradethingFuture 
from test_future.assertion.binanceFutureCryptoTable_assertion import BinanceFutureCyptoTableAssertion
from test_future.assertion.binanceFutureOpeningPositionTable_assertion import BinanceFutureOpeningPositionTableAssertion
from test_future.assertion.binanceFutureHistoryTable_assertion import BinanceFutureHistoryTableAssertion
from test_future.assertion.tradethingService_assertion import TradethingFutureServiceAssertion
from test_future.assertion.binanceService_assertion import BinanceServiceAssertion
 
                
class OpenPosition:
    _symbol_key = "symbol"
    _client_id_key = "client_id"
    _amount_base_key = "amount_b"
    _position_side_key = "position_side"
    _side_key = "side"
    
    
    def __init__(self, dynamodb: DynamoDB, bn_service:BinanceUMFutures) -> None:
        self.tradething_response: Response = None
        # dynamodb attribute
        self.bn_future_history_table = BNFutureHistoryTable(dynamodb)
        self.bn_future_opening_position_table = BNFutureOpeningPositionTable(dynamodb)
        self.bn_future_crypto_table = BNFutureCryptoTable(dynamodb)
        self.bn_future_crypto_table_before_action: list[dict] = [] 
        # binance service attribute
        self.bn_service = BnUMFuturesTrade(bn_service)
        # trade attribute
        self.tradething_future = TradethingFuture()
        # assertion attribute
        self.bn_service_assertion = BinanceServiceAssertion()  
        self.tradething_service_assertion = TradethingFutureServiceAssertion()
        self.bn_future_history_table_assert = BinanceFutureHistoryTableAssertion()
        self.bn_future_opening_position_table_assert = BinanceFutureOpeningPositionTableAssertion()
        self.bn_future_crypto_table_assert = BinanceFutureCyptoTableAssertion()

    def arrangement(self, body: dict|list[dict]) :
        if isinstance(body, dict):
            self.bn_future_crypto_table_before_action.append(self.bn_future_crypto_table.get(symbol=body[self._symbol_key]))
        else:
            for b in body:
                self.bn_future_crypto_table_before_action.append(self.bn_future_crypto_table.get(symbol=b[self._symbol_key]))

    def action(self, func: Callable, body: dict | list[dict]) :
        self.tradething_response = func(body)

    def tradething_service_assertions(self) -> TradethingFutureServiceAssertion:
        self.tradething_service_assertion.set_response(self.tradething_response)
        # assert
        return self.tradething_service_assertion

    def binance_service_assertions(self, symbol: str, request: dict):
        response = self.bn_service.get_position_inforamtion_v2(symbol=symbol)
        self.bn_service_assertion.set_response(response)
        # assert
        self.bn_service_assertion.assert_position_amount(str(request[self._amount_base_key]))
        self.bn_service_assertion.assert_position_side(request[self._position_side_key])

    def binance_future_crypto_assertions(self, symbol: str, request: dict, expected_long:int, expected_short:int):
        response = self.bn_future_crypto_table.get(symbol=symbol)
        self.bn_future_crypto_table_assert.set_response(response)
        # assert
        self.bn_future_crypto_table_assert.assert_symbol(request[self._symbol_key])
        self.bn_future_crypto_table_assert.assert_counting_long(expected_long)
        self.bnFutureCryptoAssert.assertCountingShort(expected_short)
        
    def binance_future_opening_position_assertions(self, symbol: str, position_side: str, request: dict):
        response = self.bn_future_opening_position_table.get(symbol=symbol, position_side=position_side)
        self.bn_future_opening_position_table_assert.set_response(response)
        # assert
        self.bn_future_opening_position_table_assert.assert_quantity(str(request[self._amount_base_key]))
        self.bn_future_opening_position_table_assert.assert_position_side(request[self._position_side_key])
        self.bn_future_opening_position_table_assert.assert_created_at()

    def binance_future_opening_position_assertions_for_empty(self, symbol: str, position_side: str):
        response = self.bn_future_opening_position_table.get(symbol=symbol, position_side=position_side)
        self.bn_future_opening_position_table_assert.set_response(response)
        # assert
        self.bn_future_opening_position_table_assert.assert_empty()

    
    def binance_future_history_assertions(self, client_id: str, request: dict):
        response= self.bn_future_history_table.get(client_id=client_id)
        self.bn_future_history_table_assert.set_response(response)
        # assert
        self.bn_future_history_table_assert.assert_client_id(client_id)
        self.bn_future_history_table_assert.assert_symbol(request[self._symbol_key])
        self.bn_future_history_table_assert.assert_position_side(request[self._position_side_key])
        self.bn_future_history_table_assert.assert_created_at()

    
    