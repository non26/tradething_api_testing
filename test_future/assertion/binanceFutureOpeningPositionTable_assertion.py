from decimal import Decimal

class BinanceFutureOpeningPositionTableAssertion:
    _symbolKey = "symbol"
    _sideKey = "side"
    _amountBaseKey = "amount_b"
    _positionSideKey = "position_side"
    _createdAtKey = "created_at"
    
    def __init__(self, response: dict) -> None:
        self.response = response

    def __init__(self) -> None:
        self.response = {}

    def setResponse(self, response: dict) -> None:
        self.response = response

    def assertSymbol(self, symbol: str) -> None:
        assert self.response[self._symbolKey] == symbol

    def assertSide(self, side: str) -> None:
        assert self.response[self._sideKey] == side

    def assertQuantity(self, quantity: str) -> None:
        assert Decimal(self.response[self._amountBaseKey]) == Decimal(quantity)

    def assertPositionSide(self, position_side: str) -> None:
        assert self.response[self._positionSideKey] == position_side

    def assertCreatedAt(self) -> None:
        assert self.response[self._createdAtKey] != ""