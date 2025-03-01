import boto3

s3_client = boto3.client("s3")

list_buckets_response = s3_client.list_buckets()["Buckets"]
bucket_names = ", ".join(list(map(lambda bucket: bucket["Name"], list_buckets_response)))

print(bucket_names)
