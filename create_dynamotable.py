import boto3

dynamodb = boto3.client('dynamodb', region_name='us-west-2')

table = dynamodb.create_table(
    TableName='String_Reverse',
    KeySchema=[
        {
            'AttributeName': 'Original_String',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'Reverse_String',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Original_String',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Reverse_String',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("Table status:", table)
