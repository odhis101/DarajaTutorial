# Safaricom Daraja API Vanilla Python Script for STK Push

This repository contains a Python script for initiating an STK push using the Safaricom Daraja API sandbox environment.

## Prerequisites

Before using this script, make sure you have the following:

- Python installed on your system (version 3.6 or higher)
- Requests library installed (`pip install requests`)

## Usage

1. **Clone this repository** to your local machine or download the `stk_push.py` file:

    ```
    git clone https://github.com/your-username/safaricom-daraja-vanilla-python.git
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

