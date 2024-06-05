# Automated Detection and Remediation of Exposed IAM Access Keys

This repository contains a solution to automatically detect and delete IAM access keys that are accidentally or deliberately exposed in public GitHub repositories. The solution leverages AWS Lambda, API Gateway, and SNS to automate the process and notify the DevOps team.

## Prerequisites

- AWS Account with necessary permissions
- GitHub repository
- AWS CLI configured
- Node.js and npm installed (if using AWS CDK)

## Setup Instructions

### Step 1: Set Up GitHub Webhooks

1. **Create a GitHub Webhook**:
   - Go to your GitHub repository.
   - Navigate to **Settings** > **Webhooks** > **Add webhook**.
   - Set the Payload URL to an API Gateway endpoint (we’ll create this next).
   - Choose `application/json` as the content type.
   - Select individual events or set it to trigger on `push` events, which is where the exposure is likely to happen.

### Step 2: Create an API Gateway Endpoint

1. **Create an API Gateway**:
   - In the AWS Management Console, go to **API Gateway**.
   - Create a new REST API.
   - Create a new resource and method
   - Set the integration type to **Lambda Function** 

### Step 3: Develop a Lambda Function

1. **Create a Lambda Function**:
   - Go to **AWS Lambda** in the Management Console.
   - Create a new Lambda function.
   - Choose the appropriate execution role with necessary permissions (IAM policy to list and delete access keys, send SNS notifications).

2. **Upload the Lambda Function Code**:
   - Lambda function code to handle the detection and deletion of exposed IAM keys.
   - Upload the code to the newly created Lambda function.

### Step 4: Configure IAM Role for Lambda

1. **Create an IAM Role**:
   - Go to the **IAM** section of the AWS Management Console.
   - Create a new role for the Lambda function.
   - Attach the following policies to the role:
     - `AmazonIAMFullAccess` or a custom policy with permissions to list and delete access keys.
     - `AmazonSNSFullAccess` or a custom policy with permissions to publish to SNS.
   - Assign this role to the Lambda function.

### Step 5: Configure SNS Topic

1. **Create an SNS Topic**:
   - Go to **Amazon SNS** in the Management Console.
   - Create a new topic for DevOps notifications.
   - Note the ARN of the created SNS topic.
   - Subscribe the DevOps team’s email or another notification endpoint to this topic.

### Step 6: Test the Integration

1. **Deploy and Test**:
   - Deploy the Lambda function and API Gateway.
   - Push a commit to the GitHub repository that contains an IAM access key.
   - Verify that the webhook triggers the API Gateway, which invokes the Lambda function.
   - Check that the access key is deleted and a notification is sent to the DevOps team.
