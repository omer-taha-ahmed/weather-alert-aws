# Cleanup Guide

Delete all AWS resources safely.

## Important: Do this when done!

Follow this checklist to delete all resources and prevent future charges.

## Resources to Delete

1. S3 buckets (empty first)
2. DynamoDB tables (2)
3. Lambda functions (2)
4. API Gateway
5. CloudWatch Event rule
6. SNS topic
7. IAM role

## Verification

After cleanup, check AWS Billing Dashboard shows $0.00.

## Detailed Steps

### S3
1. S3 Console → Your bucket
2. Empty bucket first
3. Delete bucket

### DynamoDB
1. DynamoDB Console
2
