
from dynamodb.dynamodb import DynamoDB, DynamoDBTable
import boto3

class BNFutureCryptoTable(DynamoDBTable):
    def __init__(self, dynamodb: DynamoDB) -> None:
        self.table_name = "bn_future_crypto"
        self.table: boto3.resource.Factory = dynamodb.table(self.table_name)
        self.content = {}
    
    def get(self, **keys) -> dict:
        """
        get the item from the table by keys: symbol={symbol}
        """
        symbolKey = "symbol"
        response: dict = self.table.get_item(Key={'symbol': keys[symbolKey].upper()})
        if 'Item' in response:
            self.content = response['Item']
        else:
            self.content = {}

    def getSymbolField(self) -> str:
        symbol = "symbol"
        return self._getFieldFromContent(symbol)
    
    def getCountingLongField(self) -> int:
        countingLong = "counting_long"
        return self._getFieldIntFromContent(countingLong)
    
    def getCountingShortField(self) -> int:
        countingShort = "counting_short"
        return self._getFieldIntFromContent(countingShort)
        
    def _getFieldFromContent(self, key: str) -> str:
        if key in self.content:
            return self.content[key]
        else:
            return ""
    
    def _getFieldIntFromContent(self, key: str) -> int:
        if key in self.content:
            return self.content[key]
        else:
            return 0
              
    # def deleteRecordBySymbol(self, symbol: str) -> None:
    #     self.table.delete_item(Key={'symbol': symbol.upper()})
            
