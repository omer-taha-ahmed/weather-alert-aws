# Deployment Guide

## Pre-Deployment Checklist

- [ ] DynamoDB tables created
- [ ] SNS topic created & email confirmed
- [ ] IAM role created
- [ ] Lambda functions deployed
- [ ] API Gateway configured
- [ ] CloudWatch Event created
- [ ] Frontend uploaded to S3
- [ ] API URL in frontend HTML

## Testing

### Test 1: Website Loads
```
Open: https://weather-alert-frontend-XXXX.s3-website-us-east-1.amazonaws.com
Expected: Page loads
```

### Test 2: Create Subscription
```bash
curl -X POST https://YOUR_API_URL/subscribe \
  -d '{"email":"test@test.com","city":"London","alertCondition":"rain"}'
Expected: {"message":"Subscription created","subscriptionId":"..."}
```

### Test 3: View Subscriptions
```bash
curl https://YOUR_API_URL/subscriptions
Expected: Array of subscriptions
```

### Test 4: Website UI
1. Open website
2. Fill form
3. Click Subscribe
4. See success message
5. Subscription appears in list

### Test 5: Email Confirmation
1. Check inbox
2. Click AWS SNS confirmation link
3. Email confirmed

## Daily Workflow (Automatic)

**8 AM UTC daily**:
1. CloudWatch Event fires
2. Lambda reads subscriptions
3. Fetches weather
4. Sends emails if conditions match
5. Saves alert history

## Monitoring

Check CloudWatch Logs:
1. Lambda Console → Monitor
2. View logs in CloudWatch
3. Check for errors

## Scaling

Current: Handles 50+ subscriptions easily
10x scale: No code changes needed, still free
100x scale: Add caching, still under $1/month

## Production Improvements

- [ ] Add user authentication
- [ ] Add custom domain
- [ ] Add CloudFront CDN
- [ ] Add CI/CD pipeline
- [ ] Add automated tests
- [ ] Add error tracking
- [ ] Add monitoring dashboard
