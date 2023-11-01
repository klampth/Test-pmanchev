import boto3

#def lambda_handler(event, context):
#    s3 = boto3.client('s3')
#    s3.upload_file(event['file_path'], event['bucket_name'], event['object_name'])

client = boto3.client('kinesisvideo')
response = client.get_data_endpoint(
    StreamName='Kinesis-Rekognition',
    APIName='GET_MEDIA'
)
print(response)
endpoint = response.get('DataEndpoint', None)
print("endpoint %s" % endpoint)

if endpoint is not None:
    client2 = boto3.client('kinesis-video-media', endpoint_url=endpoint)
    response = client2.get_media(
        StreamName='Kinesis-Rekognition',
        StartSelector={
            'StartSelectorType': 'EARLIEST',
        }
    )
    print(response)

    stream = response['Payload'] # botocore.response.StreamingBody object
    while True:
#            ret,frame = stream.read() 
            frame = stream.read()
            ret = stream.read()
            print(" stream type ret %s frame %s" % (type(ret), type(frame)))

