# Boto3 for Wasabi.com S3 Drop In Replacement
Installing `boto3_wasabi` allows you to continue to use AWS S3 with `boto3` _while_ being able to use Wasabi S3. This makes life so much easier in case you wanted to migrate data from AWS S3 to Wasabi S3 to reduce your expenses.

> Note: this is almost identical to [https://github.com/boto/boto3](https://github.com/boto/boto3). Created in response to [this support article](https://wasabi-support.zendesk.com/hc/en-us/articles/115002579891-How-do-I-use-the-AWS-SDK-for-Python-boto3-with-Wasabi-). I just replaced "boto3" with "boto3_wasabi".

## Instal using pip/pip3 
```pip install git+https://github.com/KalobMTaulien/boto3_wasabi```
```pip3 install git+https://github.com/KalobMTaulien/boto3_wasabi```
## Usage
```python
import boto3_wasabi

WASABI_ACCESS_KEY = 'your wasabi access key here'
WASABI_SECRET_KEY = 'your wasabi secret key here'
WASABI_BUCKET = 'yourbucketname'

# Create a new sample text file.
file = open('new-file.txt', 'a+')
file.write('Hello, this is my new file')
file.close()

# Open the file as readable
body = open('new-file.txt', 'rb')

# Start the boto3 client that points to Wasabi's S3 endpoints.
s3 = boto3_wasabi.client('s3', aws_access_key_id=WASABI_ACCESS_KEY, aws_secret_access_key=WASABI_SECRET_KEY)
# Upload your file
upload_data = s3.put_object(Bucket=WASABI_BUCKET, Key='your-new-filename-here.txt', Body=body, ContentType='text/plain')
# Close the file; just a good practice.
body.close()

# Print the uploaded data
print(upload_data)
```