# AWS Lambda Function: Unattached EBS Volume Manager

This AWS Lambda function helps manage unattached EBS volumes by tagging them with the current date and deleting volumes that have tags older than 14 days. It can be scheduled to run daily using Amazon CloudWatch Events.

## Prerequisites

- AWS account with necessary permissions to create and manage Lambda functions and EC2 resources.
- Python 3.x installed on your local development machine.
- AWS CLI configured with your AWS credentials.

## Setup

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/unattached-ebs-volume-manager.git
cd unattached-ebs-volume-manager
```
2. Install the required dependencies using pip:
   pip install boto3
3. Open the lambda_function.py file in a text editor and update the AWS region if needed. Modify the code as per your specific requirements.
4. Deploy the Lambda function using the AWS CLI:
5. ```bash
   aws lambda create-function --function-name unattached-ebs-volume-manager \
   --runtime python3.8 --role your-lambda-execution-role \
   --handler lambda_function.lambda_handler --zip-file fileb://lambda_function.zip
  
6. Create an Amazon CloudWatch Events rule to schedule the Lambda function to run daily:
   - Go to the AWS Management Console and navigate to CloudWatch.
   - Click on "Events" in the left navigation pane and then click on "Create rule."
   - Configure the event schedule using a cron expression to specify the daily invocation time.
   - Under "Targets," select "Lambda function" and choose the Lambda function you created in step 4.
   - Configure any additional settings required and create the CloudWatch Events rule.
  
### This code uses the Boto3 library, which is the AWS SDK for Python, to interact with AWS services. Here's a breakdown of what the code does:

1. The boto3 library is imported, and the EC2 client is created.
2. The describe_volumes API is called to find unattached EBS volumes with the status "available."
3. The current date is obtained using datetime.now().
4. Each unattached volume is tagged with the current date using the create_tags API.
5. The code then calculates a date 14 days ago and retrieves the list of unattached volumes tagged with that date.
6. Finally, the delete_volume API is called to delete each unattached volume.
