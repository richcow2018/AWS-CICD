import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    # Create the AWS clients
    ec2_client = boto3.client('ec2')

    # Find unattached EBS volumes
    response = ec2_client.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])

    # Get the current date
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Tag unattached volumes with the current date
    for volume in response['Volumes']:
        volume_id = volume['VolumeId']
        ec2_client.create_tags(Resources=[volume_id], Tags=[{'Key': 'Date', 'Value': current_date}])

    # Delete unattached volumes with tags older than 14 days
    fourteen_days_ago = datetime.now() - timedelta(days=14)
    fourteen_days_ago_str = fourteen_days_ago.strftime('%Y-%m-%d')

    response = ec2_client.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']},
                                                    {'Name': 'tag:Date', 'Values': [fourteen_days_ago_str]}])

    for volume in response['Volumes']:
        volume_id = volume['VolumeId']
        ec2_client.delete_volume(VolumeId=volume_id)
