# Lambda: Subscription Manager

Handles all subscription CRUD operations.

## Function Name
`weather-subscription-manager`

## Configuration
- Runtime: Python 3.11
- Memory: 128 MB
- Timeout: 30 seconds
- Role: weather-alert-lambda-role

## Operations

### POST /subscribe - Create
```json
{
  "email": "user@example.com",
  "city": "London",
  "alertCondition": "rain"
}
```

### GET /subscriptions - Read All
Returns array of all subscriptions

### DELETE /subscribe/{id} - Delete
Removes subscription by ID

## Database
- Table: `weather-subscriptions`
- Partition Key: `subscriptionId` (UUID)
- Attributes: email, city, alertCondition, timestamp, active
