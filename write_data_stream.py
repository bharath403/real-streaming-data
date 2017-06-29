import boto3
import json

client = boto3.client('kinesis')
i = 0
while i < 5:
    response = client.put_record(StreamName='test-stream-1', Data='foooo', PartitionKey='1111')
    print (response)
    i += 1

my_shard_id = response['ShardId']
print (my_shard_id)
