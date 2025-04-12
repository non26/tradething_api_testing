

class TradethingFutureServiceAssertion:

    def __init__(self) -> None:
        self.response = None

    def set_response(self, response: dict):
        self.response = response

    def assert_http_200(self, actual_status_code: int) -> None:
        assert actual_status_code == 200

    def assert_position(self, expected_id:str,expected_symbol:str):
        client_id_key = "clientId"
        symbol_key = "symbol"
        assert self.response[client_id_key] == expected_id
        assert self.response[symbol_key] == expected_symbol
    
    def assert_close_by_ids(self, expected_response:dict):
        message_key = "message"
        code_key = "code"
        symbol_key = "symbol"
        position_side_key = "positionSide"
        client_id_key = "clientId"
        assert self.response[message_key] == expected_response[message_key]
        assert self.response[code_key] == expected_response[code_key]
        assert self.response[symbol_key] == expected_response[symbol_key]
        assert self.response[position_side_key] == expected_response[position_side_key]
        assert self.response[client_id_key] == expected_response[client_id_key]
