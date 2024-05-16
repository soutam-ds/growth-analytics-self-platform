import utility

# Configuration
local_file_path = '/home/soutam/PycharmProjects/growth-analytics-self-platform/stm.csv'  # Replace with the path to your local file
bucket_name = 'stm-src-data'  # Replace with your S3 bucket name
s3_key = 's3://stm-src-data/Features data set.csv'  # Replace with the desired S3 key for the file

upload_file_to_s3(local_file_path, bucket_name, s3_key)