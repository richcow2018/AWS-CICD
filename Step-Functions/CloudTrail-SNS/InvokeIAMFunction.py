import boto3

def lambda_handler(event, context):
    iam_client = boto3.client('iam')
    response = iam_client.list_access_keys(UserName='example-user')
    return response
