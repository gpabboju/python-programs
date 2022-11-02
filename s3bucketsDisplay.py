import boto3

BUCKET_NAME = "s3bucketnormal-animalpics-1x7s2metp966l"

s3 = boto3.client("s3")

# List all the buckets
buckets_resp = s3.list_buckets()
for bucket in buckets_resp["Buckets"]:
    print(bucket)


