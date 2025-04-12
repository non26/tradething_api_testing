from decimal import Decimal
class BinanceServiceAssertion:
    _position_side_key = "positionSide"
    _position_amount_key = "positionAmt"

    def __init__(self) -> None:
        self.response = None
    
    def set_response(self, response: dict):
        self.response = response

    def assert_position_side(self, expected_position_side: str) -> None:
        position_side = self.response[self._position_side_key]
        assert position_side == expected_position_side

    def assert_position_amount(self, expected_position_amount: str) -> None:
        actual_position_amount = self.response[self._position_amount_key]
        actual = Decimal(actual_position_amount)
        excepted = Decimal(expected_position_amount)
        assert actual == excepted