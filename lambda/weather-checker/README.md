# Lambda: Weather Checker

Daily weather monitoring and alert system.

## Function Name
`weather-alert-checker`

## Configuration
- Runtime: Python 3.11
- Memory: 256 MB
- Timeout: 60 seconds
- Role: weather-alert-lambda-role
- Trigger: CloudWatch Events (Cron: 0 8 * * ? *)

## Daily Workflow

**8:00 AM UTC**
1. CloudWatch Event triggers this Lambda
2. Scans all subscriptions from DynamoDB
3. Fetches weather for each unique city (cached)
4. Evaluates alert conditions
5. Sends SNS emails if conditions match
6. Saves alerts to history table

## Supported Alert Conditions

- `rain` → When raining
- `snow` → When snowing
- `temp < X` → Below X°C
- `temp > X` → Above X°C
- `wind > X` → Wind above X m/s
- `cloudy` → Cloudy weather
- `clear` → Clear skies

## External APIs

- **OpenWeatherMap**: Current weather data (free tier)
  - Rate limit: 1,000 calls/day
  - API Key: 343517810cbe11fe5bae88d6a7d9498d

## Output Example
```json
{
  "subscriptions_processed": 10,
  "alerts_sent": 3
}
```
