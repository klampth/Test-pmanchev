import boto3
def lambda_handler(event, context):
    s3 = boto3.client('s3')
    s3.upload_file(event['/home/klampth/video.avi'], event['kinesis-video-datastream'], event['video.avi'])
s3 = boto3.client('s3')

s3_client = boto3.client(
    's3',
    aws_access_key_id='YOUR_ACCESS_KEY_ID',
    aws_secret_access_key='YOUR_SECRET_ACCESS_KEY'
)
#s3.upload_file(event['/home/klampth/video.avi'], event['kinesis-video-datastream'], event['video.avi'])
s3.upload_file('/home/aws_user/video.avi', 'kinesis-video-datastream', 'video.avi')
