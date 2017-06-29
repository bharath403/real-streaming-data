import boto3

client = boto3.client('kinesis')

print ("Name your stream and no of shards and relax. we will create for you")
stream = str(input())
shardcount = int(input())
response = client.create_stream(StreamName=stream,ShardCount=shardcount)
print (response)
