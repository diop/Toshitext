import dotenv
import os
from twilio.rest import Client

dotenv.load_dotenv('.env')
acccount_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(acccount_sid, auth_token)

message = client.messages \
                .create(
                    body='Get some via SMS',
                    from_='+14152002312',
                    to='+17025305234'
                )
print(message.sid)