import boto3
import json

def lambda_handler(event, context):
    sns_client = boto3.client('sns')
    response = sns_client.publish(
        TopicArn='arn:aws:sns:region:account-id:example-topic',
        Message=json.dumps(event),
        Subject='AWS Risk Credentials Exposed Alert'
    )
    return response
