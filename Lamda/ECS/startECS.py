import json
import boto3
import os

ecs_client = boto3.client('ecs')

def lambda_handler(event, context):
    # Parse the S3 event
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        # Start the ECS task
        response = ecs_client.run_task(
            cluster='your-cluster-name',
            taskDefinition='your-task-definition',
            launchType='FARGATE',
            networkConfiguration={
                'awsvpcConfiguration': {
                    'subnets': ['your-subnet-id'],
                    'assignPublicIp': 'ENABLED'
                }
            },
            overrides={
                'containerOverrides': [
                    {
                        'name': 'your-container-name',
                        'environment': [
                            {'name': 'S3_BUCKET', 'value': bucket},
                            {'name': 'S3_KEY', 'value': key}
                        ]
                    }
                ]
            }
        )
        
        print(f'Started ECS task: {response}')

    return {
        'statusCode': 200,
        'body': json.dumps('ECS task started successfully')
    }
