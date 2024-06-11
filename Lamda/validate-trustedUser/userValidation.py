import json
import boto3

def lambda_handler(event, context):
    # Extract user identity information from the event
    user_identity = event['detail']['userIdentity']
    user_arn = user_identity['arn']

    # Define trusted administrators ARNs or groups
    trusted_admins = [
        'arn:aws:iam::123456789012:user/TrustedAdmin1',
        'arn:aws:iam::123456789012:user/TrustedAdmin2'
        # Add more ARNs as needed
    ]

    # Check if the user ARN is in the list of trusted administrators
    if user_arn not in trusted_admins:
        # User is not trusted, take necessary actions
        # For example, log the event, notify the security team, etc.
        print(f"Unauthorized access detected: {user_arn}")
        # Example: send notification using SNS
        sns_client = boto3.client('sns')
        sns_client.publish(
            TopicArn='arn:aws:sns:region:account-id:topic-name',
            Message=json.dumps(event),
            Subject='Unauthorized S3 Access Detected'
        )
    else:
        print(f"Authorized access by: {user_arn}")

    return {
        'statusCode': 200,
        'body': json.dumps('Function executed successfully')
    }
