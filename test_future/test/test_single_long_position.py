from test_future.test.init import OpenPosition
from service.dynamodb.init.dynamodb import DynamoDB
from service.bn.future.binance import BinanceUMFutures

dynamodb = DynamoDB()
bn_service = BinanceUMFutures()

def clean_up_long(request: dict):
    open_position = OpenPosition(dynamodb, bn_service)
    request["side"] = "SELL"
    expected_history_table = {
        "client_id":"",
        "symbol": "",
        "position_side": "",
        "created_at": ""
    }

    open_position.arrangement(request)

    open_position.action(open_position.tradething_future.single_position_request, request)
    # opening position table test for empty result
    open_position.binance_future_opening_position_assertions_for_empty(request["symbol"], request["position_side"])
    # history table
    open_position.binance_future_history_assertions(request["client_id"], expected_history_table)


def test_buy_long_single_position():
    request = {
        "position_side": "LONG",
        "side": "BUY",
        "amount_b": "0.03",
        "symbol": "BTCUSDT",
        "client_id": "api_test_btc_long_1"
    }
    open_position = OpenPosition(dynamodb, bn_service)
    # arrangement
    open_position.arrangement(request)
    # action
    open_position.action(open_position.tradething_future.single_position_request, request)
    # assertions
    # assert tradething
    tradething_service_assertions = open_position.tradething_service_assertions()
    tradething_service_assertions.assert_http_200(200)
    tradething_service_assertions.assert_position(request["client_id"],request["symbol"])
    # assert binance
    open_position.binance_service_assertions(request["symbol"], request)
    # assert binance future crypto
    long = open_position.bn_future_crypto_table_before_action[0]["counting_long"]
    short = open_position.bn_future_crypto_table_before_action[0]["counting_short"]
    open_position.binance_future_crypto_assertions(request["symbol"], request, long+1, short)
    # assert binance future opening position
    open_position.binance_future_opening_position_assertions(request["symbol"], request["position_side"], request)
    # clean up
    clean_up_long(request)
   
def test_sell_long_single_position():
    pass

def test_duplicate_client_id_when_by_long():
    pass

def test_duplicate_client_id_when_sell_long():
    pass

def test_accumulate_long_position():
    pass

if __name__ == "__main__":
    test_buy_long_single_position()