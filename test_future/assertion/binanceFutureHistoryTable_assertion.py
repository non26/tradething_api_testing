
class BinanceFutureHistoryTableAssertion:
    _client_id_key = "client_id"
    _symbol_key = "symbol"
    _position_side_key = "position_side"
    _created_at_key = "created_at"

    def __init__(self) -> None:         
        self.response    = {}
    
    def set_response(self, response: dict) -> None:
        self.response = response

    def assert_client_id(self, expected_client_id: str) -> None:
        assert self.response[self._client_id_key] == expected_client_id

    def assert_symbol(self, expected_symbol: str) -> None:
        assert self.response[self._symbol_key] == expected_symbol
    
    def assert_position_side(self, expected_position_side: str) -> None:
        assert self.response[self._position_side_key] == expected_position_side

    def assert_created_at(self) -> None:
        assert self.response[self._created_at_key] != ""