import time
import boto3

print('Task starting..')
time.sleep(5)

s3 = boto3.resource('s3')
# Print out bucket names
lst=[]
for bucket in s3.buckets.all():
    print(bucket.name)


print('Task ended, took 5 seconds')