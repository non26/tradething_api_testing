from service.dynamodb.init.dynamodb import DynamoDB


class BNFutureOpeningPositionTable:
    def __init__(self, dynamodb: DynamoDB):
        self.table_name = "bn_future_opening_position"
        self.table = dynamodb.table(self.table_name)
        self.content = {}

    def get(self, **keys) -> dict:
        """
        get the item from the table by keys: symbol={symbol}, position_side={position_side}
        """
        symbol_key = "symbol"
        position_side_key = "position_side"
        response = self.table.get_item(Key={"symbol": keys[symbol_key].upper(), "position_side": keys[position_side_key].upper()})
        if "Item" in response:
            self.content = response["Item"]
            return self.content
        else:
            self.content = {}
            return self.content

    def get_client_id_field(self) -> str:
        client_id = "client_id"
        return self._get_field_from_content(client_id)
    
    def get_symbol_field(self) -> str:
        symbol = "symbol"
        return self._get_field_from_content(symbol)
            
    def get_amount_base_field(self) -> str:
        amount_base = "amount_b"
        return self._get_field_from_content(amount_base)

    def get_position_side_field(self) -> str:
        position_side = "position_side"
        return self._get_field_from_content(position_side)
    
    def get_side_field(self) -> str:
        side = "side"
        return self._get_field_from_content(side)
    
    def get_created_at_field(self) -> str:
        created_at = "created_at"
        return self._get_field_from_content(created_at)
        
    def _get_field_from_content(self, key: str) -> str:
        if key in self.content:
            return self.content[key]
        else:
            return ""
    