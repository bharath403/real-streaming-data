import boto3

client = boto3.client('kinesis')

print ("Tell us the stream to delete........we will delete it for you")
stream = str(input())
print ("You told us to delete", stream)
response = client.delete_stream(StreamName=stream)
print (response)
