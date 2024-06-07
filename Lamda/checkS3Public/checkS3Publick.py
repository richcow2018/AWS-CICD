import json

def lambda_handler(event, context):
    # Extract relevant information from the AWS Config event
    invoking_event = json.loads(event['invokingEvent'])
    configuration_item = invoking_event['configurationItem']
    configuration = configuration_item['configuration']
    
    # Check if the S3 bucket is public
    bucket_acl = configuration.get('accessControlList', {})
    public_access = any(
        grant['Grantee']['Type'] == 'Group' and
        'http://acs.amazonaws.com/groups/global/AllUsers' in grant['Grantee']['URI']
        for grant in bucket_acl.get('Grants', [])
    )
    
    # Determine compliance status
    compliance_type = 'NON_COMPLIANT' if public_access else 'COMPLIANT'
    
    # Return the evaluation result
    evaluation = {
        'ComplianceResourceType': configuration_item['resourceType'],
        'ComplianceResourceId': configuration_item['resourceId'],
        'ComplianceType': compliance_type,
        'OrderingTimestamp': configuration_item['configurationItemCaptureTime']
    }
    
    return {
        'evaluations': [evaluation]
    }
