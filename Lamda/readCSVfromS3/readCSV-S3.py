import boto3
import csv
import os

s3_client = boto3.client('s3')
waf_client = boto3.client('wafv2')

# Constants
BUCKET_NAME = os.environ['BUCKET_NAME']
WAF_IP_SET_ID = os.environ['WAF_IP_SET_ID']
WAF_SCOPE = 'REGIONAL'  # Change to 'CLOUDFRONT' if using WAF with CloudFront

def lambda_handler(event, context):
    # Get the uploaded file details from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Read the CSV file from S3
    response = s3_client.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8').splitlines()
    csv_reader = csv.reader(content)
    
    # Extract IP addresses
    ip_addresses = [row[0] for row in csv_reader]
    
    # Get current IP set details
    ip_set = waf_client.get_ip_set(Name=WAF_IP_SET_ID, Scope=WAF_SCOPE, Id=WAF_IP_SET_ID)
    ip_set_lock_token = ip_set['LockToken']
    
    # Update the IP set
    response = waf_client.update_ip_set(
        Name=WAF_IP_SET_ID,
        Scope=WAF_SCOPE,
        Id=WAF_IP_SET_ID,
        LockToken=ip_set_lock_token,
        Addresses=ip_addresses
    )
    
    return {
        'statusCode': 200,
        'body': 'IP set updated successfully'
    }

