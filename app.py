import dotenv
import os
import urllib
import requests, json
import gspread
import pprint
import asyncio
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from oauth2client.service_account import ServiceAccountCredentials
from blockcypher import simple_spend

dotenv.load_dotenv('.env')

app = Flask(__name__)

acccount_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
twilio_client = Client(acccount_sid, auth_token)

scope = scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
google_client = gspread.authorize(creds)

sheet = google_client.open('Toshitext').sheet1
phone_numbers = sheet.col_values(5)

commands = ['help', 'send', 'balance', 'receive', 'clear', 'cancel']

params = {'token': os.environ.get('TOKEN')}
url = 'https://api.blockcypher.com/v1/bcy/test/txs/micro'

@app.route('/')
def main():
    return 'Firebolt 💰🚀 - Send bitcoin faster and cheaper with a text message.'

@app.route('/sms', methods=['GET', 'POST'])
def inbound_sms():
    response = MessagingResponse()
    help_message = 'Help menu: help options...'
    # The phone number sending the Twilio message
    from_number = request.form['From']
    print(from_number)

    # The content of the text message
    message = request.form['Body']
    print(message)

    # Parse the text message for invidual commands
    parsed_message = message.split()
    print(parsed_message)

    # Grab the command which is the first item 
    # in the properly formatted message
    # command = parsed_message[0].lower()
    # print('command --> ', command)

    # Grab the amount which is the second item 
    # in the properly formatted message
    
    # Grab the recipient wallet address which is the third item 
    # in the properly formatted message
    
    if len(parsed_message) == 1:
        command = parsed_message[0].lower()
        if command == 'menu':
            response.message(help_message)
    elif len(parsed_message) == 3:
        privkey = sheet.cell(2,1).value

        amount = parsed_message[1]
        print('amount --> ', amount)

        recipient = parsed_message[2]
        print('address --> ', recipient)

        data = {'from_private': privkey, 'to_address': recipient, 'value_satoshis': amount}

        r = requests.post(url, data=data, params=params)
        print(r.json())

        response.message('Thanks for texting! If your phone number is registered in our system, your request will be fulfilled.')
    else:
        response.message('Your message is malformed')

    return str(response)
    
if __name__ == "__main__":
    app.run(debug=True)
    