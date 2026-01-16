# Setup Guide

Complete step-by-step deployment instructions.

## Quick Overview

1. DynamoDB: Create 2 tables
2. SNS: Create topic & subscribe email
3. IAM: Create Lambda execution role
4. Lambda: Create 2 functions with code
5. API Gateway: Create REST API with routes
6. CloudWatch: Create daily schedule trigger
7. S3: Upload frontend
8. Test everything

## Detailed Steps

See the following sections for complete instructions on each service.

### DynamoDB Tables

**weather-subscriptions**
- Partition Key: subscriptionId (String)
- Billing: Pay-per-request

**weather-alerts-history**
- Partition Key: alertId (String)
- Billing: Pay-per-request

### SNS Topic

- Topic name: weather-alerts
- Subscription: Your email address
- Protocol: Email
- Status: Confirmed

### IAM Role

- Role name: weather-alert-lambda-role
- Policies:
  - AmazonDynamoDBFullAccess
  - AmazonSNSFullAccess
  - CloudWatchLogsFullAccess

### Lambda Functions

See lambda/ folder for code and detailed configuration.

### API Gateway

- API name: weather-alert-api
- Type: REST
- Resources:
  - POST /subscribe
  - GET /subscriptions
  - DELETE /subscribe/{id}

### CloudWatch Event

- Rule name: weather-alert-daily-trigger
- Schedule: 0 8 * * ? * (8 AM UTC)
- Target: weather-alert-checker Lambda
