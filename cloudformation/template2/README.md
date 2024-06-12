# Encrypting EBS Volumes using Lambda and CloudFormation

## Step-by-Step Guide

1. **Create a Lambda Function**:
   - Develop a Lambda function that iterates through all EC2 instances in your stack, identifies attached EBS volumes, and encrypts them using KMS.

2. **Define a Custom Resource in CloudFormation**:
   - Define a Lambda-backed custom resource in your CloudFormation template. This resource will trigger the Lambda function created in the previous step.

3. **Lambda Function Execution Role**:
   - Ensure the Lambda function execution role has permissions to list EC2 instances and encrypt EBS volumes using KMS.

4. **CloudFormation Stack Template**:
   - Add the custom resource to your CloudFormation stack template. Specify the S3 bucket name and the key (filename) of the Lambda function ZIP file using `S3Bucket` and `S3Key` respectively.

## Notes on S3Key Property

The `S3Key` property in the CloudFormation template refers to the name of the ZIP file containing your Lambda function code stored in an Amazon S3 bucket. When creating a Lambda function, package your function code and any dependencies into a ZIP file, then upload it to an S3 bucket.

Ensure to replace placeholders like `your-lambda-zip-file.zip` with the actual key (filename) of the ZIP file containing your Lambda function code.

## In the CloudFormation template, S3Key: your-lambda-zip-file.zip would be replaced with the actual key (filename) of the ZIP file containing your Lambda function code. For example, if your Lambda function code is in a file named lambda_function.py and you zipped it into a file named my-lambda-function.zip, then S3Key would be my-lambda-function.zip.

### Here's how it works:

1. You upload your Lambda function code ZIP file to an S3 bucket.
2. In the CloudFormation template, you specify the S3 bucket name using S3Bucket, and the key (filename) of the ZIP file using S3Key.
3. When you create the CloudFormation stack, CloudFormation retrieves the Lambda function code from the specified S3 bucket using the provided key.
