import boto3
import os

os.environ['AWS_PROFILE'] = "iamadmin-general"
os.environ['AWS_DEFAULT_REGION'] = "us-east-1"

ec2 = boto3.client('ec2')

# Retrieves all regions/endpoints that work with ec2
response = ec2.describe_regions()
print('Regions:', response['Regions'])

