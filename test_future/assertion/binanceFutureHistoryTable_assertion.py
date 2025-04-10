
class BinanceFutureHistoryTableAssertion:
    _clientIdKey = "client_id"
    _symbolKey = "symbol"
    _positionSideKey = "position_side"
    _createdAtKey = "created_at"

    def __init__(self, response: dict) -> None:         
        self.response    = response

    def __init__(self) -> None:         
        self.response    = {}
    
    def setResponse(self, response: dict) -> None:
        self.response = response

    def assertClientId(self, expected_client_id: str) -> None:
        assert self.response[self._clientIdKey] == expected_client_id

    def assertSymbol(self, expected_symbol: str) -> None:
        assert self.response[self._symbolKey] == expected_symbol
    
    def assertPositionSide(self, expected_position_side: str) -> None:
        assert self.response[self._positionSideKey] == expected_position_side

    def assertCreatedAt(self) -> None:
        assert self.response[self._createdAtKey] != ""