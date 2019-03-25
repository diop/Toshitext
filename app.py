import dotenv
import os
import urllib
import requests, json
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from blockcypher import simple_spend



dotenv.load_dotenv('.env')

app = Flask(__name__)

acccount_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(acccount_sid, auth_token)

@app.route('/')
def index():
    return 'Firebolt API vAlpha'

@app.route('/sms', methods=['GET', 'POST'])
def inbound_sms():
    '''Respond to incoming messages with a friendly SMS.'''
    response = MessagingResponse()
    response.message('Thanks for texting! If your phone number is registered in our system, your request will be fulfilled')

    body = urllib.parse.quote(request.form['Body'])

    command_args = body.lower().split()

    from_number = request.form['From']
    to_number = request.form['To']

    return str(response)
    
if __name__ == "__main__":
    app.run(debug=True)
    