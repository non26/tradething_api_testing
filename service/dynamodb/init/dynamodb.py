import boto3
from abc import ABC, abstractmethod
import os

class DynamoDB:
    def __init__(self) -> None:
        self.dynamodb  = boto3.resource(
            'dynamodb',
            aws_access_key_id=os.getenv('DYNAMODB_SECRET_KEY'), 
            aws_secret_access_key=os.getenv('DYNAMODB_ACCESS_KEY'), 
            region_name=os.getenv('DYNAMODB_REGION'),
            endpoint_url=os.getenv('DYNAMODB_ENDPOINT'))

    def table(self, table_name: str):
        return self.dynamodb.Table(table_name)

class DynamoDBTable(ABC):
    @abstractmethod
    def get(self, **keys) -> dict:
        pass
    
    

