# AWS Config and AWS Lambda Integration

## Overview

This repository demonstrates how AWS Config can be configured to invoke AWS Lambda functions. This integration allows for automated, custom remediation of non-compliant resources in your AWS environment. By using AWS Config rules and AWS Lambda, you can ensure that your resources remain compliant with your organization’s policies and best practices.

## How It Works

1. **AWS Config Rules**: These rules evaluate the configuration of your AWS resources. Custom rules can be created to check for specific conditions.
2. **AWS Lambda**: A compute service that lets you run code without provisioning or managing servers. Lambda functions can be triggered by AWS Config when resources are found to be non-compliant.
3. **Remediation Actions**: Lambda functions can perform remediation actions, such as updating security group rules, based on the evaluation results from AWS Config.

## Example Use Case

Consider a scenario where you want to ensure that no security groups have port 22 (SSH) open to the public. If a security group is found to be non-compliant, you want to automatically restrict access to port 22 to only your office’s public IP address.

## Step-by-Step Setup

### Step 1: Create a Lambda Function

Create a Lambda function that will update security group rules to restrict SSH access.

### Step 2: Create a Custom AWS Config Rule
## Create a custom AWS Config rule to check for security groups with port 22 open to the public.

Config Rule Definition
1. Open the AWS Config console.
2. Create a new rule and select Custom Lambda Rule.
3. Provide a name and description for the rule.
4. Specify the resource type as AWS::EC2::SecurityGroup.
5. Select the Lambda function created in Step 1.

### Step 3: Set Up Permissions
## Ensure the Lambda function has the necessary permissions to interact with AWS Config and EC2.

IAM Policy for Lambda
Attach the following IAM policy to the Lambda execution role:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:RevokeSecurityGroupIngress",
                "config:PutEvaluations"
            ],
            "Resource": "*"
        }
    ]
}
```

### Step 4: Configure AWS Config to Use the Lambda Function

1. In the AWS Config console, go to the rule you created.
2. Specify the Lambda function as the remediation action.
3. Configure the trigger for the rule (e.g., configuration changes, periodic).

### Testing

1. Create a security group with port 22 open to the public (0.0.0.0/0).
2. AWS Config should detect the non-compliance based on the custom rule.
3. AWS Config triggers the Lambda function.
4. The Lambda function updates the security group to restrict port 22 to your office's public IP address.

