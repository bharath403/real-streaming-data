from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

table = dynamodb.Table('String_Reverse')

response = table.put_item(
           Item={
               'Original_String': 'foo',
               'Reverse_String': 'oof',
            }
        )

print (response)
