from service.dynamodb.dynamodb import DynamoDB


class BNFutureHistoryTable:
    def __init__(self, dynamodb: DynamoDB):
        self.table_name = "bn_future_history"
        self.table = dynamodb.table(self.table_name)
        self.content = {}

    def get(self, **keys) -> dict:
        """
        get the item from the table by keys: client_id={client_id}
        """
        client_id_key = "client_id"
        response = self.table.get_item(Key={client_id_key: keys[client_id_key].upper()})
        if "Item" in response:
            self.content = response["Item"]
            return self.content
        else:
            self.content = {}
            return self.content


    def get_client_id_field(self) -> str:
        client_id_key = "client_id"
        return self._get_field_from_content(client_id_key)
    
    def get_symbol_field(self) -> str:
        symbol_key = "symbol"
        return self._get_field_from_content(symbol_key)
    
    def get_position_side_field(self) -> str:
        position_side_key = "position_side"
        return self._get_field_from_content(position_side_key)

    def get_created_at_field(self) -> str:
        created_at_key = "created_at"
        return self._get_field_from_content(created_at_key)

    def _get_field_from_content(self, key: str) -> str:
        if key in self.content:
            return self.content[key]
        return ""
    