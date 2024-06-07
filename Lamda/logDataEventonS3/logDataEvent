import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    
    # Process the event as needed
    # For simplicity, we're just logging the event to CloudWatch Logs
    
    return {
        'statusCode': 200,
        'body': json.dumps('Event logged successfully')
    }
