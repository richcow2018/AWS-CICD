# Securely Managing Database Credentials in Amazon ECS

This guide demonstrates how to securely store and use database credentials in an Amazon ECS task using AWS Secrets Manager and AWS KMS.

## Overview

1. **AWS Secrets Manager**: Store and encrypt database credentials.
2. **AWS KMS**: Encrypt the credentials.
3. **IAM Role**: Create an IAM role for ECS task execution with permissions to access AWS Secrets Manager and KMS.
4. **ECS Task Definition**: Reference the secrets in the task definition.

## Prerequisites

- AWS account with appropriate permissions.
- AWS CLI installed and configured.

## Step-by-Step Guide

### Step 1: Store Database Credentials in AWS Secrets Manager

1. Open the [AWS Secrets Manager Console](https://console.aws.amazon.com/secretsmanager/).
2. Click on "Store a new secret".
3. Select "Other type of secret".
4. Add your database credentials (e.g., `username` and `password`).
5. Choose an encryption key (default AWS managed key or a custom KMS key).
6. Click "Next".
7. Provide a name for the secret (e.g., `MyDatabaseCredentials`).
8. Optionally, add tags and resource permissions.
9. Click "Next" and then "Store".

### Step 2: Create an IAM Role for ECS Task Execution

1. Open the [IAM Console](https://console.aws.amazon.com/iam/).
2. Click on "Roles" and then "Create role".
3. Select "AWS service" and then "Elastic Container Service".
4. Select "Elastic Container Service Task" and click "Next: Permissions".
5. Attach the following policies:
   - **SecretsManagerReadWrite**: Allows the ECS task to read secrets.
   - **AmazonECSTaskExecutionRolePolicy**: Allows the ECS task to pull container images and write to CloudWatch Logs.
   - **kms:Decrypt**: Allows the ECS task to decrypt secrets encrypted with KMS. Create a custom policy if needed.
6. Click "Next: Tags", then "Next: Review".
7. Name the role (e.g., `ECSTaskExecutionRole`) and click "Create role".

### Step 3: Reference IAM Role in ECS Task Definition

1. Open the [Amazon ECS Console](https://console.aws.amazon.com/ecs/).
2. Go to "Task Definitions" and click "Create new Task Definition".
3. Select "Fargate" or "EC2" based on your use case.
4. Under "Task execution role", select the role created in Step 2 (`ECSTaskExecutionRole`).
5. Add your container definitions.

### Step 4: Specify Secrets in Container Definition

In the container definition, specify the secrets to be passed to the container:

1. In the "Container Definitions" section, add a container or edit an existing one.
2. Under "Environment", click "Add environment variable".
3. Choose "ValueFrom" and enter the ARN of the secret stored in AWS Secrets Manager.

Example:

- **Name**: `DB_USERNAME`
- **ValueFrom**: `arn:aws:secretsmanager:us-east-1:123456789012:secret:MyDatabaseCredentials-ABC123`

You can specify multiple secrets by adding more environment variables.

### Example JSON Task Definition Snippet
