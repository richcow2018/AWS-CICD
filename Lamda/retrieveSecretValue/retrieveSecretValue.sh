#!/bin/bash

secret_name="your-secret-name"  # Replace with your actual secret name
region="your-region"  # Replace with your AWS region

# Retrieve the secret value using AWS CLI
secret_value=$(aws secretsmanager get-secret-value --secret-id $secret_name --region $region --query SecretString --output text)

# Set the secret value as an environment variable
export SECRET_VALUE=$secret_value

# Run your application
python your_application.py
