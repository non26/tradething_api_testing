from requests import Response
from test_future.test_future import OpenPosition


def test_open_long_single_position():
   long = {
    "position_side": "LONG",
    "side": "SELL",
    "amount_b": "0.03",
    "symbol": "BTCUSDT",
    "client_id": "test_btc_long_1"
       }

def test_close_long_multiple_position():
    pass

def duplicate_client_id_when_open_position():
    pass

def duplicate_client_id_when_close_position():
    pass

def test_open_long_multiple_position():
    pass

def test_close_long_single_position():
    pass


def test_accumulate_long_position():
    pass
