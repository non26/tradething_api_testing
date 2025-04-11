from decimal import Decimal
class BinanceServiceAssertion:
    _position_side_key = "position_side"
    _position_amount_key = "position_amount"

    def __init__(self) -> None:
        self.response = None
    
    def set_response(self, response: dict):
        self.response = response

    def assert_position_side(self, expected_position_side: str) -> None:
        assert self.response[self._position_side_key] == expected_position_side

    def assert_position_amount(self, expected_position_amount: str) -> None:
        actual_position_amount = self.response[self._position_amount_key]
        assert Decimal(actual_position_amount) == Decimal(expected_position_amount)