import boto3

ecs_client = boto3.client('ecs')
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Check if the S3 bucket is empty
    response = s3_client.list_objects_v2(Bucket='your-bucket-name')
    
    if 'Contents' not in response:
        # Stop all running ECS tasks in the cluster
        tasks = ecs_client.list_tasks(cluster='your-cluster-name', desiredStatus='RUNNING')
        
        if tasks['taskArns']:
            ecs_client.stop_task(cluster='your-cluster-name', task=tasks['taskArns'][0])
            print(f'Stopped task: {tasks["taskArns"][0]}')

    return {
        'statusCode': 200,
        'body': json.dumps('Checked for idle tasks and stopped if necessary')
    }
