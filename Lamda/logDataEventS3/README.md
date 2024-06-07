# AWS S3 Activity Logging with CloudTrail and Lambda

This project demonstrates how to monitor and log actions on S3 objects (such as PUT, GET, and DELETE operations) using AWS CloudTrail, Lambda, and CloudWatch. The setup ensures that all S3 data events are logged and can be reviewed for auditing purposes.

## Overview

1. **CloudTrail**: Tracks and stores S3 API call logs.
2. **Lambda**: Processes CloudTrail events and logs them to CloudWatch Logs.
3. **CloudWatch Events**: Triggers the Lambda function for specific S3 actions.

## Prerequisites

- AWS account with appropriate permissions.
- AWS CLI installed and configured.

## Step-by-Step Setup

### Step 1: Create an S3 Bucket for CloudTrail Logs

1. Go to the [Amazon S3 Console](https://console.aws.amazon.com/s3/).
2. Create a new S3 bucket (e.g., `cloudtrail-logs-your-bucket-name`).

### Step 2: Enable CloudTrail for S3 Data Events

1. Open the [AWS CloudTrail Console](https://console.aws.amazon.com/cloudtrail/).
2. Click on "Trails" in the left navigation pane.
3. Click on "Create trail".
4. Fill in the necessary details:
   - **Trail name**: `S3DataEventsTrail`
   - **S3 bucket**: Use the bucket created in Step 1.
5. Under "Management events", ensure read/write events are enabled as needed.
6. Under "Data events", click "Add S3 bucket" and specify the bucket with the confidential files. Enable logging for "All S3 actions".
7. Click "Create".

### Step 3: Create a Lambda Function to Log Data Events

1. Open the [AWS Lambda Console](https://console.aws.amazon.com/lambda/).
2. Click on "Create function".
3. Choose "Author from scratch".
4. Enter a name for your function (e.g., `LogS3DataEvents`).
5. Choose the runtime as Python (e.g., Python 3.9).
6. Under "Permissions", choose "Create a new role with basic Lambda permissions".

#### Lambda Function Code

Create a file named `lambda_function.py` with the following code:

```python
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
```

### Step 4: Set Up Permissions for the Lambda Function
Ensure the Lambda function has the necessary permissions to log to CloudWatch Logs.

Attach the following IAM policy to the Lambda execution role:


### Step 5: Create a CloudWatch Events Rule
1. Open the CloudWatch Console.
2. Go to "Rules" under "Events".
3. Click on "Create rule".
4. Configure the rule as follows:
5. Event Source: Select "AWS services" and then "CloudTrail".
6. Targets: Add the Lambda function you created (e.g., LogS3DataEvents).
7. Click on "Create rule".

### Step 6: Verify CloudTrail is Logging S3 Data Events
Upload, download, and delete objects in your S3 bucket to generate events.
Go to the CloudTrail console and verify that these actions are being logged.

### Step 7: Verify Lambda Logs in CloudWatch
1. Open the CloudWatch Console.
2. Go to "Logs" in the left navigation pane.
3. Find the log group corresponding to your Lambda function (e.g., /aws/lambda/LogS3DataEvents).
4. Verify that the logs contain the details of the S3 events.
