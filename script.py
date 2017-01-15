import os.path
import os
import sys
from pathlib import Path
import boto
import boto.s3
import sys
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = 'AKIAJSDV7UIS2YYE2ZGA'
AWS_SECRET_ACCESS_KEY = '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'

bucket_name = 'azhack2017'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)


bucket = conn.create_bucket(bucket_name,
	location=boto.s3.connection.Location.DEFAULT)

fileName = 'newEvent.txt'
myFile = Path("/Users/swatimunjal/Downloads/"+fileName)
while not myFile.is_file():
	continue

file = open(fileName, "r+")
data = file.read()
file.close()
print data
s3File = 'records.txt'
#get file from s3
for key in bucket.list():
    print key.name
    key.get_contents_to_filename('/Users/swatimunjal/Downloads/downloaded.txt')

with open('/Users/swatimunjal/Downloads/Downloaded.txt', "r+") as myfile:
    body = myfile.read()
#print 'Body: '+ body
#print 'data: '+ data
data = body+data
#append
with open(s3File, "w") as myfile:
    myfile.write('*'+data+'*')


testfile = s3File
print 'Uploading %s to Amazon S3 bucket %s' % \
   (testfile, bucket_name)

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()


k = Key(bucket)
k.key = 'my test file'
k.set_contents_from_filename(testfile,
    cb=percent_cb, num_cb=10)

os.remove("newEvent.txt")
os.remove("records.txt")
os.remove("downloaded.txt")