
from service.dynamodb.init.dynamodb import DynamoDB, DynamoDBTable
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
        symbol_key = "symbol"
        response: dict = self.table.get_item(Key={"symbol": keys[symbol_key].upper()})
        if "Item" in response:
            self.content = response["Item"]
            return self.content
        else:
            self.content = {}
            return self.content

    def get_symbol_field(self) -> str:
        symbol = "symbol"
        return self._get_field_from_content(symbol)
    
    def get_counting_long_field(self) -> int:
        counting_long = "counting_long"
        return self._get_field_int_from_content(counting_long)
    
    def get_counting_short_field(self) -> int:
        counting_short = "counting_short"
        return self._get_field_int_from_content(counting_short)
        
    def _get_field_from_content(self, key: str) -> str:
        if key in self.content:
            return self.content[key]
        else:
            return ""
    
    def _get_field_int_from_content(self, key: str) -> int:
        if key in self.content:
            return self.content[key]
        else:
            return 0
              
    # def deleteRecordBySymbol(self, symbol: str) -> None:
    #     self.table.delete_item(Key={'symbol': symbol.upper()})
            
