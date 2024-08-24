import boto3

client = boto3.client("connect")
response = client.list_instances(['ResponseMetadata'][''])
print(response)