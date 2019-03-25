from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Ahoy! Thanks so much for your message.")
    # message = client.messages \
    #                 .create(
    #                     body='Get some via SMS',
    #                     from_='+14152002312',
    #                     to='+17025305234'
    #                 )
    # print(message.sid)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)