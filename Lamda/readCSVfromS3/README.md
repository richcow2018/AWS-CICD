# AWS Lambda IP Whitelisting Solution

## Overview

This repository contains a solution for automating IP whitelisting for a suite of web applications hosted on AWS. The solution uses an AWS Lambda function to update an AWS WAF IP set based on a CSV file containing proxy IP addresses stored in an S3 bucket. The IP addresses are refreshed twice a month by the network team.

## Architecture

1. **S3 Bucket**: Stores the CSV file with proxy IP addresses.
2. **Lambda Function**: Reads the CSV file from S3, extracts the IP addresses, and updates the AWS WAF IP set.
3. **Trigger**: An S3 event triggers the Lambda function whenever a new CSV file is uploaded.

## Prerequisites

- AWS Account
- IAM Role for Lambda with necessary permissions
- S3 Bucket for storing CSV files
- AWS WAF IP set created

## Deployment Steps

### 1. Create the S3 Bucket

Create an S3 bucket to store the CSV file with proxy IP addresses.

### 2. Create the AWS WAF IP Set

Create an AWS WAF IP set that will be updated by the Lambda function.

### 3. Deploy the Lambda Function

#### Create the Lambda Function

1. Open the AWS Lambda console.
2. Create a new Lambda function.
3. Copy and paste the provided Lambda function code into the Lambda console.
4. Set the following environment variables for the Lambda function:
   - `BUCKET_NAME`: The name of your S3 bucket.
   - `WAF_IP_SET_ID`: The ID of your AWS WAF IP set.

#### Set IAM Permissions

Ensure the Lambda function's execution role has the following permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "wafv2:GetIPSet",
        "wafv2:UpdateIPSet"
      ],
      "Resource": "*"
    }
  ]
}
```

### 4. Configure S3 Event Notification
#### Configure an S3 event notification to trigger the Lambda function whenever a new CSV file is uploaded:

1. Open the S3 bucket in the AWS Management Console.
2. Go to the Properties tab.
3. Add an event notification with the following settings:
- Event Name: (e.g., NewCSVUpload)
- Event Types: All object create events
- Destination: Lambda function
- Lambda Function: Your newly created Lambda function

### 5.Testing

1. Upload a sample CSV file with the required format to the S3 bucket.
2. Verify that the Lambda function is triggered and updates the AWS WAF IP set accordingly.
