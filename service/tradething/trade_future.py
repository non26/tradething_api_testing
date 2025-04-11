import os
import requests
from requests import Response

class TradethingFuture:
    def __init__(self):
        self._trade_thing_url = os.getenv("TRADETHING_URL") + os.getenv("FUTURES_TRADETHING_PREFIX")

    def single_position_request(self, body: dict) -> Response:
        path = "/position"
        return self._send_request(body, path)
    
    def multiple_position_request(self, body: list[dict]) -> Response:
        path = "/positions"
        response: Response = self._send_request(body, path)
        return response
    
    def close_by_ids_request(self, ids: dict) -> Response:
        path = "/close-by-ids"
        response: Response = self._send_request(ids, path)
        return response
    
    def _send_request(self, body: dict | list[dict], path: str) -> Response:
        response: Response = requests.post(self._trade_thing_url + path, json=body, timeout=10)
        return response
    
    