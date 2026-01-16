# Cost Analysis

## Monthly Breakdown

| Service | Free Limit | Our Usage | Cost |
|---------|-----------|-----------|------|
| Lambda | 1M invocations | 80 | $0.00 |
| DynamoDB | 25GB | 50MB | $0.00 |
| SNS | 1,000 emails | 30 | $0.00 |
| API Gateway | 1M requests | 690 | $0.00 |
| S3 | 5GB | 1MB | $0.00 |
| CloudWatch | Unlimited | 1 rule | $0.00 |
| **TOTAL** | — | — | **$0.00** |

## Scaling Costs

**1,000 subscriptions**: ~$0.50/month
**10,000 subscriptions**: ~$1/month
**100,000 subscriptions**: ~$15/month
**1M subscriptions**: ~$50/month

## Cost Optimization

- Use on-demand pricing (not provisioned)
- Cache weather data (reduce API calls)
- Batch DynamoDB operations
- Monitor usage regularly

## Comparison

AWS: $0.00/month
Heroku: $7-50/month
DigitalOcean: $5-50/month
Traditional VPS: $10-50/month

**Winner: AWS by far!**
