import json
import boto3
import requests
from datetime import datetime
import uuid

# Configuration
OPENWEATHER_API_KEY = '343517810cbe11fe5bae88d6a7d9498d'
SNS_TOPIC_ARN = 'REPLACE_WITH_YOUR_SNS_ARN'

dynamodb = boto3.resource('dynamodb')
subscriptions_table = dynamodb.Table('weather-subscriptions')
alerts_table = dynamodb.Table('weather-alerts-history')
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    """
    Daily weather checker triggered by CloudWatch Events.
    
    Runs at: 8 AM UTC daily
    Process:
    1. Read all subscriptions
    2. Fetch weather for each city
    3. Evaluate alert conditions
    4. Send SNS emails if condition matches
    5. Save alert to history
    """
    try:
        response = subscriptions_table.scan()
        subscriptions = response.get('Items', [])
        
        print(f"Processing {len(subscriptions)} subscriptions")
        
        checked_cities = {}
        alerts_sent = 0
        
        for subscription in subscriptions:
            city = subscription['city']
            email = subscription['email']
            alert_condition = subscription['alertCondition']
            
            # Fetch weather (cache by city)
            if city not in checked_cities:
                weather_data = get_weather(city)
                if weather_data:
                    checked_cities[city] = weather_data
                else:
                    print(f"Failed to get weather for {city}")
                    continue
            else:
                weather_data = checked_cities[city]
            
            # Check if alert condition is met
            should_alert, message = check_condition(alert_condition, weather_data, city)
            
            if should_alert:
                send_alert(email, message)
                save_alert(email, city, message)
                alerts_sent += 1
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'subscriptions_processed': len(subscriptions),
                'alerts_sent': alerts_sent
            })
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def get_weather(city):
    """Fetch current weather from OpenWeatherMap API"""
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': OPENWEATHER_API_KEY,
            'units': 'metric'
        }
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Weather API error for {city}: {str(e)}")
        return None

def check_condition(alert_condition, weather_data, city):
    """Check if alert condition is met"""
    try:
        temp = weather_data['main']['temp']
        condition = weather_data['weather'][0]['main'].lower()
        wind_speed = weather_data['wind']['speed']
        
        alert_lower = alert_condition.lower().strip()
        
        if alert_lower == "rain" and condition == "rain":
            return True, f"⚠️ Rain Alert: Rain in {city}! Temp: {temp}°C"
        
        if alert_lower == "snow" and condition == "snow":
            return True, f"⚠️ Snow Alert: Snow in {city}! Temp: {temp}°C"
        
        if alert_lower.startswith("temp <"):
            threshold = float(alert_lower.split('<')[1].strip())
            if temp < threshold:
                return True, f"⚠️ Cold Alert: {temp}°C in {city} (below {threshold}°C)"
        
        if alert_lower.startswith("temp >"):
            threshold = float(alert_lower.split('>')[1].strip())
            if temp > threshold:
                return True, f"⚠️ Hot Alert: {temp}°C in {city} (above {threshold}°C)"
        
        if alert_lower.startswith("wind >"):
            threshold = float(alert_lower.split('>')[1].strip())
            if wind_speed > threshold:
                return True, f"⚠️ Wind Alert: {wind_speed} m/s in {city}"
        
        if alert_lower == "cloudy" and "cloud" in condition:
            return True, f"⚠️ Cloudy in {city}"
        
        if alert_lower == "clear" and condition == "clear":
            return True, f"☀️ Clear skies in {city}!"
        
        return False, ""
    
    except Exception as e:
        print(f"Condition check error: {str(e)}")
        return False, ""

def send_alert(email, message):
    """Send SNS email notification"""
    try:
        sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject='🌤️ Weather Alert',
            Message=message
        )
        print(f"Alert sent to {email}")
    except Exception as e:
        print(f"Failed to send alert: {str(e)}")

def save_alert(email, city, message):
    """Save alert to history table"""
    try:
        alert_id = str(uuid.uuid4())
        alerts_table.put_item(Item={
            'alertId': alert_id,
            'email': email,
            'city': city,
            'message': message,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        print(f"Failed to save alert: {str(e)}")
