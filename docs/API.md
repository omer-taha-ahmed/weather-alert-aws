# API Documentation

## Base URL
```
https://YOUR_API_GATEWAY_URL/prod
```

## Endpoints

### POST /subscribe
Create subscription
```json
{
  "email": "user@example.com",
  "city": "London",
  "alertCondition": "rain"
}
```
Response: `{"message":"Subscription created","subscriptionId":"..."}`

### GET /subscriptions
Get all subscriptions
```json
[
  {
    "subscriptionId": "...",
    "email": "user@example.com",
    "city": "London",
    "alertCondition": "rain",
    "timestamp": "2024-01-15T10:30:00",
    "active": true
  }
]
```

### DELETE /subscribe/{id}
Delete subscription
Response: `{"message":"Subscription deleted"}`

## Alert Conditions

- `rain` → When raining
- `snow` → When snowing
- `temp < 5` → Below 5°C
- `temp > 30` → Above 30°C
- `wind > 10` → Wind above 10 m/s
- `cloudy` → Cloudy weather
- `clear` → Clear skies

## Error Codes

| Code | Message |
|------|---------|
| 201 | Subscription created |
| 200 | Success |
| 400 | Bad request (missing fields) |
| 404 | Not found (invalid endpoint) |
| 500 | Server error |

## cURL Examples
```bash
# Create
curl -X POST https://YOUR_API_URL/subscribe \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","city":"London","alertCondition":"rain"}'

# Get all
curl https://YOUR_API_URL/subscriptions

# Delete
curl -X DELETE https://YOUR_API_URL/subscribe/SUBSCRIPTION_ID
```
