# Safaricom Daraja API Vanilla Python Script for STK Push

This repository contains a Python script for initiating an STK push using the Safaricom Daraja API sandbox environment.

## Prerequisites

Before using this script, make sure you have the following:

- Python installed on your system (version 3.6 or higher)
- Requests library installed (`pip install requests`)

## Usage

1. **Clone this repository** to your local machine or download the `stk_push.py` file:

    ```
    git clone https://github.com/odhis101/DarajaTutorial
    ```

2. **Navigate to the project directory**:

    ```
    cd safaricom-daraja-vanilla-python
    ```

3. **Open the `stk_push.py` file** in a text editor.

4. **Replace the placeholder values** with your actual Safaricom Daraja API credentials and parameters:

    ```python
    YOUR_CONSUMER_KEY = 'YourConsumerKey'
    YOUR_CONSUMER_SECRET = 'YourConsumerSecret'
    YOUR_SHORTCODE = 'YourShortcode'
    YOUR_PASSKEY = 'YourPasskey'
    YOUR_PHONE_NUMBER = 'PhoneNumberToReceiveSTKPush'
    YOUR_AMOUNT = '100'  # Replace with the desired amount
    YOUR_CALLBACK_URL = 'YourCallbackURL'
    ```

5. **Save the changes** to the `stk_push.py` file.

6. **Run the Python script**:

    ```
    python stk_push.py
    ```

7. The script will initiate an STK push using the provided parameters and display the result.

## Additional Notes

- Ensure that your callback URL is accessible and configured to receive transaction status updates from Safaricom.
- This script is intended for use in the Safaricom Daraja API sandbox environment. Be sure to switch to the production environment and update the endpoint URL accordingly when deploying for production use.



# Safaricom Daraja API Flask Endpoint for STK Push

This repository contains a Flask API endpoint for initiating an STK push using the Safaricom Daraja API sandbox environment.

## Prerequisites

Before using this endpoint, make sure you have the following:

- Python installed on your system (version 3.6 or higher)
- Flask installed (`pip install flask`)
- Requests library installed (`pip install requests`)

## Usage

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/odhis101/DarajaTutorial
    ```

2. Navigate to the project directory:

    ```
    cd safaricom-daraja-flask-endpoint
    ```

3. Run the Flask application:

    ```
    python app.py
    ```

4. Once the application is running, you can send a POST request to the `/stkpush` endpoint with the required parameters:

    - `consumer_key`: Your Safaricom Daraja API consumer key
    - `consumer_secret`: Your Safaricom Daraja API consumer secret
    - `shortcode`: Your Safaricom Daraja API shortcode
    - `passkey`: Your Safaricom Daraja API passkey
    - `phone_number`: The phone number to receive the STK push
    - `amount`: The amount to be transacted
    - `callback_url`: The callback URL to receive transaction status updates

    Example request body:

    ```json
    {
        "consumer_key": "YOUR_CONSUMER_KEY",
        "consumer_secret": "YOUR_CONSUMER_SECRET",
        "shortcode": "YOUR_SHORTCODE",
        "passkey": "YOUR_PASSKEY",
        "phone_number": "PHONE_NUMBER_TO_RECEIVE_STK_PUSH",
        "amount": "100",
        "callback_url": "YOUR_CALLBACK_URL"
    }
    ```

5. Send the POST request to the `/stkpush` endpoint using your preferred HTTP client (e.g., Postman, cURL).

6. You will receive a JSON response containing the result of the STK push initiation.

## Additional Notes

- Make sure to replace the placeholder values (`YOUR_CONSUMER_KEY`, `YOUR_CONSUMER_SECRET`, `YOUR_SHORTCODE`, `YOUR_PASSKEY`, `PHONE_NUMBER_TO_RECEIVE_STK_PUSH`, `YOUR_CALLBACK_URL`) with your actual Safaricom Daraja API credentials and parameters.
- Ensure that your callback URL is accessible and configured to receive transaction status updates from Safaricom.
- This endpoint is intended for use in the Safaricom Daraja API sandbox environment. Be sure to switch to the production environment and update the endpoint URL accordingly when deploying for production use.


