import boto3

def lambda_handler(event, context):
    cloudtrail_client = boto3.client('cloudtrail')
    response = cloudtrail_client.lookup_events(
        LookupAttributes=[
            {
                'AttributeKey': 'Username',
                'AttributeValue': 'example-user'
            },
        ]
    )
    return response
