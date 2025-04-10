import boto3
from abc import ABC, abstractmethod


class DynamoDB:
    def __init__(self) -> None:
        self.dynamodb: _  = boto3.resource('dynamodb')

    def table(self, table_name: str) -> boto3.resource.Factory:
        return self.dynamodb.Table(table_name)

class DynamoDBTable(ABC):
    @abstractmethod
    def get(self, **keys) -> dict:
        pass
    
    

