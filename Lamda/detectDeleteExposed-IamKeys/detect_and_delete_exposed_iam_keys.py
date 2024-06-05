import json
import boto3
import requests
import re

# Initialize AWS clients
iam_client = boto3.client('iam')
sns_client = boto3.client('sns')
sns_topic_arn = 'arn:aws:sns:region:account-id:devops-notifications'

# Function to delete the exposed IAM access key
def delete_access_key(username, access_key_id):
    response = iam_client.delete_access_key(
        UserName=username,
        AccessKeyId=access_key_id
    )
    return response

# Function to send SNS notification
def send_notification(message):
    response = sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=message,
        Subject='Exposed IAM Access Key Detected'
    )
    return response

def lambda_handler(event, context):
    # Parse the GitHub event payload
    payload = json.loads(event['body'])
    commits = payload['commits']
    
    access_key_pattern = re.compile(r'AKIA[0-9A-Z]{16}')
    
    for commit in commits:
        modified_files = commit['modified'] + commit['added']
        
        for file in modified_files:
            raw_url = file['raw_url']
            response = requests.get(raw_url)
            if response.status_code == 200:
                content = response.text
                matches = access_key_pattern.findall(content)
                for access_key in matches:
                    # Retrieve the associated IAM user for the access key
                    try:
                        user_info = iam_client.get_access_key_last_used(AccessKeyId=access_key)
                        username = user_info['UserName']
                        # Delete the exposed access key
                        delete_access_key(username, access_key)
                        # Send notification to the DevOps team
                        message = f"Access key {access_key} for user {username} was exposed and has been deleted."
                        send_notification(message)
                    except Exception as e:
                        print(f"Error processing access key {access_key}: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps('Processing complete')
    }
