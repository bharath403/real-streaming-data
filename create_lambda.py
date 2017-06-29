import boto3
import base64
client = boto3.client('lambda')

response = client.create_function(
    FunctionName='lambda-testing',
    Runtime='python3.6',
    Role='arn:aws:iam::738261200374:role/AAALambdaTestRole',
    Handler='sample.lambda_handler',
    Code={
        'ZipFile': base64.b64decode('/home/vagrant/lambda.zip'),
    },
    Description='This is a lambda test function',
    Timeout=3,
    MemorySize=128,
)

print (response)
