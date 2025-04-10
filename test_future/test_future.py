from requests import Response
from typing import Callable      
from service.bn.future.trade import BnUMFuturesTrade
from service.dynamodb.future.bn_future_crypto_table import BNFutureCryptoTable
from service.dynamodb.future.bn_future_history_table import BNFutureHistoryTable
from service.dynamodb.future.bn_future_opening_position_table import BNFutureOpeningPositionTable
from service.tradething.trade_future import TradethingFuture 
from assertion.binanceFutureCryptoTable_assertion import BinanceFutureCyptoTableAssertion
from assertion.binanceFutureOpeningPositionTable_assertion import BinanceFutureOpeningPositionTableAssertion
from assertion.binanceFutureHistoryTable_assertion import BinanceFutureHistoryTableAssertion
from assertion.tradethingService_assertion import TradethingFutureServiceAssertion
from assertion.binanceService_assertion import BinanceServiceAssertion
 
                
class OpenPosition:
    _symbolKey = "symbol"
    _clientIdKey = "client_id"
    _amountBaseKey = "amount_b"
    _positionSideKey = "position_side"
    _sideKey = "side"
    
    
    def __init__(self) -> None:
        self.tradethingResponse: Response = None
        # dynamodb attribute
        self.bnFutureHistoryTable = BNFutureHistoryTable()
        self.bnFutureOpeningPositionTable = BNFutureOpeningPositionTable()
        self.bnFutureCryptoTable = BNFutureCryptoTable()
        self.bnFutureCryptoTableBeforeAction: list[dict] = [] 
        # binance service attribute
        self.bnService = BnUMFuturesTrade()
        # trade attribute
        self.tradethingFuture = TradethingFuture()
        # assertion attribute
        self.bnServiceAssertion = BinanceServiceAssertion()  
        self.tradethingServiceAssertion = TradethingFutureServiceAssertion()
        self.bnFutureHistoryTableAssert = BinanceFutureHistoryTableAssertion()
        self.bnFutureOpeningPositionTableAssert = BinanceFutureOpeningPositionTableAssertion()
        self.bnFutureCryptoTableAssert = BinanceFutureCyptoTableAssertion()

    def arrangement(self, bodyList: list[dict]) :
        for body in bodyList:
            self.bnFutureCryptoTableBeforeAction.append(self.bnFutureCryptoTable.getPosition(body[self._symbolKey]))

    def action(self, func: Callable, body: dict | list[dict]) :
        self.tradethingResponse = func(body)

    def tradethingServiceAssertions(self) -> TradethingFutureServiceAssertion:
        # assert
       return self.tradethingServiceAssertion

    def binanceServiceAssertions(self, symbol: str, request: dict):
        response = self.bnService.get_position_inforamtion_v2(symbol=symbol)
        self.bnServiceAssertion.setResponse(response)
        # assert
        self.bnServiceAssertion.assertPositionAmount(str(request[self._amountBaseKey]))
        self.bnServiceAssertion.assertPositionSide(request[self._positionSideKey])

    def binanceFutureCryptoAssertions(self, symbol: str, request: dict, expected_long:int, expected_short:int):
        response = self.bnFutureCryptoTable.get(symbol=symbol)
        self.bnFutureCryptoTableAssert.setResponse(response)
        # assert
        self.bnFutureCryptoAssert.assertSymbol(request[self._symbolKey])
        self.bnFutureCryptoAssert.assertCountingLong(expected_long)
        self.bnFutureCryptoAssert.assertCountingShort(expected_short)
        
    def binanceFutureOpeningPositionAssertions(self, symbol: str, positionSide: str, request: dict):
        response = self.bnFutureOpeningPositionTable.get(symbol=symbol, position_side=positionSide)
        self.bnFutureOpeningPositionTableAssert.setResponse(response)
        # assert
        self.bnFutureOpeningPositionAssert.assertQuantity(str(request[self._amountBaseKey]))
        self.bnFutureOpeningPositionAssert.assertPositionSide(request[self._positionSideKey])
        self.bnFutureOpeningPositionAssert.assertCreatedAt()
    
    def binanceFutureHistoryAssertions(self, clientId: str, request: dict):
        response= self.bnFutureHistoryTable.get(client_id=clientId)
        self.bnFutureHistoryTableAssert.setResponse(response)
        # assert
        self.bnFutureHistoryAssert.assertClientId(clientId)
        self.bnFutureHistoryAssert.assertSymbol(request[self._symbolKey])
        self.bnFutureHistoryAssert.assertPositionSide(request[self._positionSideKey])
        self.bnFutureHistoryAssert.assertCreatedAt()
    
    
