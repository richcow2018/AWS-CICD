import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances()

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            for volume in instance['BlockDeviceMappings']:
                if volume.get('Ebs'):
                    params = {
                        'VolumeId': volume['Ebs']['VolumeId'],
                        'KmsKeyId': 'your-kms-key-id'
                    }
                    ec2.modify_volume(**params)

    return "EBS volumes encrypted successfully."
