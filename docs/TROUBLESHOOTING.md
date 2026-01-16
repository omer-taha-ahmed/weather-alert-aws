# Troubleshooting

## Issue 1: "Missing Authentication Token"

**Cause**: API URL wrong or API not deployed

**Fix**:
1. API Gateway → Stages → prod
2. Copy Invoke URL
3. Update in frontend HTML
4. Hard refresh browser

## Issue 2: Subscriptions Not Showing

**Cause**: API URL wrong or cache not cleared

**Fix**:
1. Update API URL in HTML
2. Hard refresh: Ctrl+F5
3. Check browser console (F12) for errors

## Issue 3: Email Not Received

**Cause**: SNS email not confirmed

**Fix**:
1. SNS Console → Topics → weather-alerts
2. Subscriptions → Your email
3. Check status
4. Confirm link if PendingConfirmation

## Issue 4: Form Gives Error

**Cause**: Missing fields or invalid email

**Fix**:
1. Fill all fields
2. Email must be valid (user@example.com)
3. Select condition from dropdown

## Issue 5: Daily Alerts Not Sending

**Cause**: Conditions don't match weather

**Fix**:
1. Check actual weather (Google)
2. Compare with your condition
3. If no match = no alert (correct!)

## Issue 6: Lambda Timeout

**Cause**: Timeout too short

**Fix**:
1. Lambda Console → General configuration
2. Timeout → 60 seconds
3. Save

## Issue 7: CORS Error

**Cause**: CORS not enabled

**Fix**:
1. API Gateway → Resources
2. Click "Enable CORS" on all resources
3. Deploy to prod stage

## Issue 8: "Table Not Found"

**Cause**: DynamoDB table doesn't exist

**Fix**:
1. DynamoDB Console → Tables
2. Create missing tables:
   - weather-subscriptions
   - weather-alerts-history

## Issue 9: AccessDenied Error

**Cause**: Lambda role missing permissions

**Fix**:
1. IAM → Roles
2. Select your Lambda role
3. Attach: AmazonDynamoDBFullAccess
4. Attach: AmazonSNSFullAccess

## Issue 10: Website Blank

**Cause**: S3 not configured for static hosting

**Fix**:
1. S3 → Properties
2. Static website hosting → Enable
3. Index document: index.html
4. Save

## Quick Checklist

- [ ] Website loads?
- [ ] API URL correct?
- [ ] Cache cleared (Ctrl+F5)?
- [ ] API deployed?
- [ ] CORS enabled?
- [ ] DynamoDB tables exist?
- [ ] Lambda permissions correct?
- [ ] SNS email confirmed?
- [ ] CloudWatch Event created?

**Check CloudWatch Logs for detailed errors!**
