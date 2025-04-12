from decimal import Decimal

class BinanceFutureOpeningPositionTableAssertion:
    _symbol_key = "symbol"
    _side_key = "side"
    _amount_base_key = "amount_b"
    _position_side_key = "position_side"
    _created_at_key = "created_at"
    

    def __init__(self) -> None:
        self.response = {}

    def set_response(self, response: dict) -> None:
        self.response = response

    def assert_symbol(self, symbol: str) -> None:
        assert self.response[self._symbol_key] == symbol

    def assert_side(self, side: str) -> None:
        assert self.response[self._side_key] == side

    def assert_quantity(self, quantity: str) -> None:
        assert Decimal(self.response[self._amount_base_key]) == Decimal(quantity)

    def assert_position_side(self, position_side: str) -> None:
        assert self.response[self._position_side_key] == position_side

    def assert_created_at(self) -> None:
        assert self.response[self._created_at_key] != ""

    def assert_empty(self) -> None:
        assert self.response[self._symbol_key] == ""
        assert self.response[self._side_key] == ""
        assert self.response[self._amount_base_key] == ""
        assert self.response[self._position_side_key] == ""
        assert self.response[self._created_at_key] == ""