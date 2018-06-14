import boto3
from botocore.client import Config
ACCESS_KEY_ID = 'AKIAJKZJPQW77VXMHMIA'
ACCESS_SECRET_KEY = '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'

mybucket = input('enter bucket name: ')

BUCKET_NAME = mybucket

s3 = boto3.client('s3')

s3.delete_bucket(Bucket = BUCKET_NAME)

print('done')
