import boto3

client = boto3.client("s3")
response = client.list_buckets()
#print(range(len(response)))
for i in range(len(response) -1):
    print(response['Buckets'][i]['Name'])
print(type(response))
#print(dir(response))