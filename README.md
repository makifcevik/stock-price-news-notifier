# Stock Price and News Notifier

This Python script provides a simple tool for monitoring daily stock price changes and receiving relevant news articles for a specified company. It uses Alpha Vantage for stock price data and News API for news articles.

## Features

- Retrieve daily stock price data for a chosen company.
- Calculate the percentage change in stock price.
- Fetch and display relevant news articles related to the chosen company.
- Send notifications via SMS using Twilio when significant stock price changes occur.

## Usage

1. Clone this repository to your local machine.

2. Install the required Python libraries using pip:

   ```bash
   
   pip install requests twilio
   

3. Obtain API keys for Alpha Vantage and News API. Replace the placeholders in the script with your own API keys.

4. Configure your Twilio account with your credentials (ACCOUNT_SID, AUTH_TOKEN, FROM_NUMBER, TO_NUMBER).

5. Run the script:

   ```bash
   
   python main.py
   

6. The script will provide stock price information, calculate percentage changes, and send SMS notifications when significant price changes occur.

## Dependencies
- requests: For making API requests.
- twilio: For sending SMS notifications.

## Additional Notes
- To get the sms messages dailiy, you need to run your script everyday manually. Or you can use an external tool like https://www.pythonanywhere.com to make it automatically for you.




