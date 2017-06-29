import boto3
import json
from datetime import datetime
import time

my_stream_name = 'test-stream-1'

kinesis_client = boto3.client('kinesis', region_name='us-west-2')

my_shard_id = 'shardId-000000000000'

shard_iterator = kinesis_client.get_shard_iterator(StreamName=my_stream_name,
                                                      ShardId=my_shard_id,
                                                      ShardIteratorType='LATEST')

my_shard_iterator = shard_iterator['ShardIterator']

record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator,
                                              Limit=5)

while 'NextShardIterator' in record_response:
    record_response = kinesis_client.get_records(ShardIterator=record_response['NextShardIterator'],
                                                  Limit=5)

    print (record_response)

    # wait for 5 seconds
    time.sleep(5)
