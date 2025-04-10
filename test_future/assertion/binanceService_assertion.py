from decimal import Decimal
class BinanceServiceAssertion:
    _positionSideKey = "positionSide"
    _positionAmountKey = "positionAmount"

    def __init__(self, response: dict) -> None:
        self.response: dict = response

    def __init__(self) -> None:
        self.response = None
    
    def setResponse(self, response: dict):
        self.response = response

    def assertPositionSide(self, expected_position_side: str) -> None:
        assert self.response[self._positionSideKey] == expected_position_side

    def assertPositionAmount(self, expected_position_amount: str) -> None:
        actual_position_amount = self.response[self._positionAmountKey]
        assert Decimal(actual_position_amount) == Decimal(expected_position_amount)