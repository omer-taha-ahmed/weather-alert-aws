# Architecture Deep Dive

## System Design

### High-Level Flow
```
User → Website → API Gateway → Lambda → DynamoDB
                                  ↓
                          OpenWeatherMap API
                                  ↓
                                Lambda
                                  ↓
                              SNS Topic
                                  ↓
                            User Email
```

### Components

**Frontend**: HTML/CSS/JS on S3
**API**: API Gateway REST endpoints
**Compute**: Lambda (2 functions)
**Database**: DynamoDB (2 tables)
**Email**: SNS (email notifications)
**Scheduler**: CloudWatch Events (daily 8 AM UTC)
**External**: OpenWeatherMap API (weather data)

### Data Models

**weather-subscriptions**
- subscriptionId (PK): UUID
- email: string
- city: string
- alertCondition: string
- timestamp: ISO string
- active: boolean

**weather-alerts-history**
- alertId (PK): UUID
- email: string
- city: string
- message: string
- timestamp: ISO string

## Why This Architecture?

✓ Serverless = no servers to manage
✓ Event-driven = automatic daily checks
✓ Scalable = handles millions of requests
✓ Cost-effective = free tier sufficient
✓ Reliable = AWS managed services
✓ Fast = millisecond response times
