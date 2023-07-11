import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv
import os
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
AWS_REGION_NAME = os.getenv('AWS_REGION_NAME')

def upload_file_to_s3(file, folder, filename):
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION_NAME
    )

    try:
        s3.upload_fileobj(file, AWS_BUCKET_NAME, f"{folder}/{filename}")
        file_url = f"https://{AWS_BUCKET_NAME}.s3.amazonaws.com/{folder}/{filename}"
        return file_url
    except NoCredentialsError:
        return None
        