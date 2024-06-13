# AWS Lambda and CloudWatch Events Integration

This guide explains how to integrate AWS Lambda and CloudWatch Events to schedule a daily process that searches for unauthorized Amazon Machine Images (AMIs) among running Amazon EC2 instances within your VPC. The integration will automatically take the necessary actions, such as notifying the Security and Development teams and terminating the unauthorized instances.

## Prerequisites

Before you begin, ensure you have the following:

- An AWS account with appropriate permissions to create and configure Lambda functions, CloudWatch Events, and SNS topics.
- Basic knowledge of AWS services, IAM roles, and programming.
- Familiarity with the Python programming language (or your preferred language).

## Steps

Follow these steps to integrate AWS Lambda and CloudWatch Events:

1. **Set up an Amazon SNS topic:**

   - Create an Amazon SNS topic to which you'll publish messages. This topic will inform the Security and Development teams about unauthorized AMIs. Take note of the ARN (Amazon Resource Name) of the created SNS topic.

2. **Create an IAM role for the Lambda function:**

   - Create an IAM role with the necessary permissions to access EC2 instances, terminate instances, and publish messages to the SNS topic.
   - Attach the `AmazonEC2ReadOnlyAccess` policy to allow read-only access to EC2 instances.
   - Attach the `AmazonSNSPublishPolicy` policy to allow publishing messages to the SNS topic.
   - Take note of the IAM role ARN for use in the Lambda function.

3. **Create a Lambda function:**

   - Go to the AWS Management Console and open the Lambda service.
   - Click "Create function" and choose the "Author from scratch" option.
   - Provide a name, select the runtime as "Python" (or your preferred language), and choose the IAM role you created in the previous step.
   - In the function code, write the logic to search for unauthorized AMIs among running EC2 instances.
   - When an unauthorized AMI is found, publish a message to the SNS topic using the `boto3` AWS SDK and specify the issue occurred.
   - Also, terminate the EC2 instance using the `terminate_instances` method from the `boto3` SDK.
   - Save the Lambda function.

4. **Set up a CloudWatch Events rule:**

   - Go to the CloudWatch service in the AWS Management Console.
   - Click on "Rules" in the left navigation pane and then click "Create rule."
   - In the rule configuration, set the schedule expression to run the rule daily at the desired time.
   - Add a target for the rule and select the Lambda function you created as the target.
   - Save the CloudWatch Events rule.

## Conclusion

By following these steps, you have successfully integrated AWS Lambda and CloudWatch Events to schedule a daily process that searches for unauthorized AMIs among running EC2 instances within your VPC. Whenever an unauthorized AMI is found, a message will be published to the specified SNS topic, and the Lambda function will automatically terminate the unauthorized EC2 instance.

Please ensure you test and validate the solution in a controlled environment before deploying it to production.
