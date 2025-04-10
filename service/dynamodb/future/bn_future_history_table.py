from dynamodb.dynamodb import DynamoDB


class BNFutureHistoryTable:
    def __init__(self, dynamodb: DynamoDB):
        self.table_name = "bn_future_history"
        self.table = dynamodb.table(self.table_name)
        self.content = {}

    
    def get(self, **keys) -> dict:
        """
        get the item from the table by keys: client_id={client_id}
        """
        clientIdKey = "client_id"
        response = self.table.get_item(Key={'client_id': keys[clientIdKey].upper()})
        if 'Item' in response:
            return response['Item']
        else:
            return {}


    def getClientIdField(self) -> str:
        clientId = "client_id"
        return self._getFieldFromContent(clientId)
    
    def getSymbolField(self) -> str:
        symbol = "symbol"
        return self._getFieldFromContent(symbol)
        
    def getPositionSideField(self) -> str:
        positionSide = "position_side"
        return self._getFieldFromContent(positionSide)
        
    def getCreatedAtField(self) -> str:
        createdAt = "created_at"
        return self._getFieldFromContent(createdAt)
        
    def _getFieldFromContent(self, key: str) -> str:
        if key in self.content:
            return self.content[key]
        else:
            return ""