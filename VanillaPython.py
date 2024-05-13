import requests
import base64
from datetime import datetime

# Function to get access token
def get_access_token(consumer_key, consumer_secret):
    url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    auth = base64.b64encode(f'{consumer_key}:{consumer_secret}'.encode()).decode()
    headers = {'Authorization': f'Basic {auth}'}
    response = requests.get(url, headers=headers)
    return response.json().get('access_token')

# Function to initiate STK push
def initiate_stk_push(consumer_key, consumer_secret, shortcode, passkey, phone_number, amount, callback_url):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    access_token = get_access_token(consumer_key, consumer_secret)
    url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    password = base64.b64encode(f'{shortcode}{passkey}{timestamp}'.encode()).decode()
    headers = {'Authorization': f'Bearer {access_token}'}
    payload = {
        'BusinessShortCode': shortcode,
        'Password': password,
        'Timestamp': timestamp,
        'TransactionType': 'CustomerPayBillOnline',
        'Amount': amount,
        'PartyA': phone_number,
        'PartyB': shortcode,
        'PhoneNumber': phone_number,
        'CallBackURL': callback_url,
        'AccountReference': 'Test',
        'TransactionDesc': 'Test Payment'
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Example usage
if __name__ == '__main__':
    consumer_key = 'YOUR_CONSUMER_KEY'
    consumer_secret = 'YOUR_CONSUMER_SECRET'
    shortcode = 'YOUR_SHORTCODE'
    passkey = 'YOUR_PASSKEY'
    phone_number = 'YOUR_PHONE_NUMBER'
    amount = '100'  # Replace with the desired amount
    callback_url = 'YOUR_CALLBACK_URL'

    stk_push_response = initiate_stk_push(consumer_key, consumer_secret, shortcode, passkey, phone_number, amount, callback_url)
    print(stk_push_response)
