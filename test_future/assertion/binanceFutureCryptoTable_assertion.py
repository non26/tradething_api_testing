class BinanceFutureCyptoTableAssertion:
    _symbolKey = "symbol"
    _countingLongKey = "counting_long"
    _countingShortKey = "counting_short"

    def __init__(self, response: dict) -> None:
        self.response = response

    def __init__(self) -> None:
        self.response = {}

    def setResponse(self, response: dict) -> None:
        self.response = response

    def assertSymbol(self, symbol: str) -> None:
        assert self.response[self._symbolKey] == symbol

    def assertCountingLong(self, expected_counting_long: int) -> None:
        assert self.response[self._countingLongKey] == expected_counting_long

    def assertCountingShort(self, expected_counting_short: int) -> None:
        assert self.response[self._countingShortKey] == expected_counting_short