import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
subscriptions_table = dynamodb.Table('weather-subscriptions')

def lambda_handler(event, context):
    """
    Handler for subscription management endpoints.
    
    Routes:
    - POST /subscribe → Create subscription
    - GET /subscriptions → List all subscriptions
    - GET /subscribe → Alias for /subscriptions
    - DELETE /subscribe/{id} → Delete subscription
    """
    try:
        http_method = event.get('httpMethod', '')
        path = event.get('path', '')
        
        # Parse body safely (GET requests have no body)
        body_str = event.get('body')
        body = json.loads(body_str) if body_str else {}
        
        # POST /subscribe - Create subscription
        if http_method == 'POST' and path == '/subscribe':
            return create_subscription(body)
        
        # GET /subscriptions - List all subscriptions
        elif http_method == 'GET' and path == '/subscriptions':
            return list_subscriptions()
        
        # GET /subscribe - Alias for /subscriptions
        elif http_method == 'GET' and path == '/subscribe':
            return list_subscriptions()
        
        # DELETE /subscribe/{id} - Delete subscription
        elif http_method == 'DELETE' and '/subscribe/' in path:
            subscription_id = path.split('/')[-1]
            return delete_subscription(subscription_id)
        
        return response(404, {'error': 'Endpoint not found'})
        
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return response(500, {'error': str(e)})

def create_subscription(body):
    """Create a new weather alert subscription"""
    email = body.get('email', '').strip()
    city = body.get('city', '').strip()
    alert_condition = body.get('alertCondition', '').strip()
    
    if not all([email, city, alert_condition]):
        return response(400, {'error': 'Missing: email, city, alertCondition'})
    
    subscription_id = str(uuid.uuid4())
    
    subscriptions_table.put_item(Item={
        'subscriptionId': subscription_id,
        'email': email,
        'city': city,
        'alertCondition': alert_condition,
        'timestamp': datetime.now().isoformat(),
        'active': True
    })
    
    return response(201, {
        'message': 'Subscription created',
        'subscriptionId': subscription_id
    })

def list_subscriptions():
    """List all subscriptions"""
    response_data = subscriptions_table.scan()
    items = response_data.get('Items', [])
    return response(200, items)

def delete_subscription(subscription_id):
    """Delete a subscription"""
    subscriptions_table.delete_item(Key={'subscriptionId': subscription_id})
    return response(200, {'message': 'Subscription deleted'})

def response(status_code, body):
    """Format response with CORS headers"""
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(body)
    }
