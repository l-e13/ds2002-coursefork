#!/bin/python3

import urllib.request

# ask for URL
url = input("Please enter the URL for the file you would like to fetch: ")

# name the file
file_name  = "lab4_downloaded_file.gif"

# save the file
urllib.request.urlretrieve(url, file_name)

# upload to s3
import boto3

# create client
s3 = boto3.client('s3', region_name = 'us-east-1')

# upload to your bucket
bucket = 'ds2002-jww2fj'
local_file  = 'projects/lab4_downloaded_file.gif'

with open(file_name,'rb') as file:
      s3.put_object(
      Body = file,
      Bucket = bucket,
      Key = local_file,
      ACL = 'public-read',
      ContentType = 'image/gif')


# Presign URL
bucket_name = bucket
object_name = local_file
expires_in = 604800

response = s3.generate_presigned_url('get_object',
Params={'Bucket': bucket_name, 'Key': object_name}, 
ExpiresIn=expires_in)

# Output URL
print(response)

# Presigned URL: https://ds2002-jww2fj.s3.amazonaws.com/projects/lab4_downloaded_file.gif?AWSAccessKeyId=ASIAZQ3DOMJMV7NWTV4N&Signature=RR4owGRbPy5YGUQYEJFTIXI%2FGPc%3D&x-amz-security-token=FwoGZXIvYXdzEDEaDMTxN6qy3wFVpVvhRyLEAfccJr5aaVy8U0014yNpnzjdnyv0wqu90RcP9Z2zy%2BP2xWJPIKoCDPx1b1iURt4EFGIZ8fdMkHOnv219sbGdMp%2B%2FiYxhKK9c%2FUdPaMeNc9V7Y4GewKCcMM6Rz%2B2EttghDXPcjJjyQfTxZsu6jvWRX%2BBfTtDl2GLZBfC3%2BjEAuXlKtGysgElIpJwePKEVxWmJIxG3J40cdAwgFDA5Y%2B3G%2B5pxP%2BW%2FDyy4KDCB2GjmwyaEPe%2FcqSToO7QaQnKoSQwi3amuAloo59KCrwYyLSa4IPw50Qt3%2FcpDMdNfgeWN8J%2BNICWA39gjtte7vbdT3bhEILks8Yz6xh2uhg%3D%3D&Expires=1709828059
