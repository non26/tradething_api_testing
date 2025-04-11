class BinanceFutureCyptoTableAssertion:
    _symbol_key = "symbol"
    _counting_long_key = "counting_long"
    _counting_short_key = "counting_short"

    def __init__(self) -> None:
        self.response = {}

    def set_response(self, response: dict) -> None:
        self.response = response

    def assert_symbol(self, symbol: str) -> None:
        assert self.response[self._symbol_key] == symbol

    def assert_counting_long(self, expected_counting_long: int) -> None:
        assert self.response[self._counting_long_key] == expected_counting_long

    def assert_counting_short(self, expected_counting_short: int) -> None:
        assert self.response[self._counting_short_key] == expected_counting_short