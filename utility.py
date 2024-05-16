
## aws connectivity

import boto3

def upload_file_to_s3(local_file_path, bucket_name, s3_key):
    # Initialize the S3 client
    s3_client = boto3.client('s3')

    try:
        # Upload the file to S3
        s3_client.upload_file(local_file_path, bucket_name, s3_key)
        print(f"File uploaded successfully to s3://{bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")



upload_file_to_s3(local_file_path, bucket_name, s3_key)


