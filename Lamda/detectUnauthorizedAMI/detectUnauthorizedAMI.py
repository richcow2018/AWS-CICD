import boto3

def lambda_handler(event, context):
    # Create an EC2 client
    ec2_client = boto3.client('ec2')

    # Get a list of running EC2 instances
    response = ec2_client.describe_instances(
        Filters=[
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )

    # Iterate over the instances and check for unauthorized AMIs
    unauthorized_instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            ami_id = instance['ImageId']
            # Perform your unauthorized AMI check logic here
            if unauthorized_ami_check(ami_id):
                unauthorized_instances.append(instance['InstanceId'])
                # Publish message to SNS topic
                publish_to_sns(instance)
                # Terminate the unauthorized EC2 instance
                terminate_instance(ec2_client, instance['InstanceId'])

    if unauthorized_instances:
        print(f"Unauthorized AMIs found in instances: {unauthorized_instances}")
    else:
        print("No unauthorized AMIs found.")

def unauthorized_ami_check(ami_id):
    # Implement your unauthorized AMI check logic here
    # Return True if the AMI is unauthorized, False otherwise
    # Example: Check if the AMI is in a predefined list of authorized AMIs
    authorized_amis = ['ami-12345678', 'ami-87654321']
    return ami_id not in authorized_amis

def publish_to_sns(instance):
    # Create an SNS client
    sns_client = boto3.client('sns')

    # Specify the ARN of the SNS topic
    sns_topic_arn = 'arn:aws:sns:us-east-1:123456789012:UnauthorizedAMIAlert'

    # Publish message to the SNS topic
    sns_client.publish(
        TopicArn=sns_topic_arn,
        Subject='Unauthorized AMI Alert',
        Message=f"Unauthorized AMI found in instance: {instance['InstanceId']}"
    )

def terminate_instance(ec2_client, instance_id):
    # Terminate the EC2 instance
    ec2_client.terminate_instances(InstanceIds=[instance_id])
