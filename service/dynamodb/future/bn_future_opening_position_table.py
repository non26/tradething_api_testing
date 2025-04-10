from dynamodb.dynamodb import DynamoDB


class BNFutureOpeningPositionTable:
    def __init__(self, dynamodb: DynamoDB):
        self.table_name = "bn_future_opening_position"
        self.table = dynamodb.table(self.table_name)
        self.content = {}

    def get(self, **keys) -> dict:
        """
        get the item from the table by keys: symbol={symbol}, position_side={position_side}
        """
        symbolKey = "symbol"
        positionSideKey = "position_side"
        response = self.table.get_item(Key={'symbol': keys[symbolKey].upper(), 'position_side': keys[positionSideKey].upper()})
        if 'Item' in response:
            self.content = response['Item']
        else:
            self.content = {}

    def getClientIdField(self) -> str:
        clientId = "client_id"
        return self._getFieldFromContent(clientId)
    
    def getSymbolField(self) -> str:
        symbol = "symbol"
        return self._getFieldFromContent(symbol)
            
    def getAmountBaseField(self) -> str:
        amountBase = "amount_b"
        return self._getFieldFromContent(amountBase)

    def getPositionSideField(self) -> str:
        positionSide = "position_side"
        return self._getFieldFromContent(positionSide)
    
    def getSideField(self) -> str:
        side = "side"
        return self._getFieldFromContent(side)
    
    def getCreatedAtField(self) -> str:
        createdAt = "created_at"
        return self._getFieldFromContent(createdAt)
        
    def _getFieldFromContent(self, key: str) -> str:
        if key in self.content:
            return self.content[key]
        else:
            return ""
    