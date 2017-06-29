import boto3
import json
from datetime import datetime
import calendar
import random
import time

my_stream_name = 'test-stream-1'

kinesis_client = boto3.client('kinesis', region_name='us-west-2')

def put_to_stream(string_id, string_value, string_timestamp):
    payload = {
                'string_value': str(string_value),
                'string_timestamp': str(string_timestamp),
                'string_id': int(string_id)
              }

    print (payload)

    put_response = kinesis_client.put_record(
                        StreamName=my_stream_name,
                        Data=json.dumps(payload),
                        PartitionKey='1')

print ("How many strings you want to reverse")
j = int(input())
i = 0 
while i < j:
    print ("Please input the String you want to Reverse")
    string_value = input()
    string_timestamp = calendar.timegm(datetime.utcnow().timetuple())
    string_id = random.randint(40, 120)

    put_to_stream(string_id, string_value, string_timestamp)
    i += 1
    # wait for 5 second
    time.sleep(1)
