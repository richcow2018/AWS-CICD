#!/bin/bash
INSTANCE_ID=$(curl -s http://169.254.169.254/latest/meta-data/instance-id)
TARGET_GROUP_ARN="arn:aws:elasticloadbalancing:region:account-id:targetgroup/target-group-name/target-group-id"
STATUS=$(aws elbv2 describe-target-health --target-group-arn $TARGET_GROUP_ARN --targets Id=$INSTANCE_ID --query 'TargetHealthDescriptions[*].TargetHealth.State' --output text)

if [ "$STATUS" != "healthy" ]; then
  echo "Instance is not healthy"
  exit 1
fi

echo "Instance is healthy"
exit 0
