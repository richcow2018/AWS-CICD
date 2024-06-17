import boto3

def get_secret_value():
    secret_name = "your-secret-name"  # Replace with your actual secret name
    region_name = "your-region"  # Replace with your AWS region

    # Create a Secrets Manager client
    client = boto3.client("secretsmanager", region_name=region_name)

    # Retrieve the secret value
    response = client.get_secret_value(SecretId=secret_name)

    # Extract the secret value from the response
    if "SecretString" in response:
        secret_value = response["SecretString"]
    else:
        # Handle binary secret values if applicable
        secret_value = response["SecretBinary"]

    return secret_value
