

class TradethingFutureServiceAssertion:

    def __init__(self) -> None:
        pass


    def assert_http_200(self, actual_status_code: int) -> None:
        assert actual_status_code == 200

    def assert_position(self, actual_id:str, expected_id:str, actual_symbol:str, expected_symbol:str):
        assert actual_id == expected_id
        assert actual_symbol == expected_symbol
    
    def assert_close_by_ids(self,actual_response: dict, expected_response:dict):
        message_key = "message"
        code_key = "code"
        symbol_key = "symbol"
        position_side_key = "positionSide"
        client_id_key = "clientId"
        assert actual_response[message_key] == expected_response[message_key]
        assert actual_response[code_key] == expected_response[code_key]
        assert actual_response[symbol_key] == expected_response[symbol_key]
        assert actual_response[position_side_key] == expected_response[position_side_key]
        assert actual_response[client_id_key] == expected_response[client_id_key]
