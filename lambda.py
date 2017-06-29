from __future__ import print_function
import boto3
import json
import base64
def lambda_handler(event, context):
    for record in event['Records']:
        payload=base64.b64decode(record["kinesis"]["data"])
        payload = json.loads(payload)
        
    original_string = (payload['string_value'])
    
        
    x = len(original_string)
    reverse_string = ""
    for i in range(1,x+1):
        reverse_string += original_string[x-i] 
    
    print ("Original_String:",original_string,"Reverse_String:",reverse_string)
    
    
    
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

    table = dynamodb.Table('String_Reverse')

    response = table.put_item(
           Item={
               'Original_String': original_string,
               'Reverse_String': reverse_string,
            }
        )

    #print (response)
    #print (reverse_string)
    #print (original_string[x-i],end="")
        
    return "Success"  
    
    
