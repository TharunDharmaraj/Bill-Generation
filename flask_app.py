from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from images import image
from threading import Thread


app = Flask(__name__)

# account_sid = 'AC2083a270cc1f28d7b1b445449cb0e65d'
# auth_token = '01ac8f1526ea48e2cb03c3e27bab1796'
account_sid = 'YOUR_TWILLIO_ID'
auth_token = 'TWILLIO_ACCESS_TOKEN'
client = Client(account_sid, auth_token)


def sendDM(body_mess, image_url):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=body_mess,
        media_url=image_url,
        # to='whatsapp:+14039985310'
        to='whatsapp:WHATSAPP_NUMBER_TO_BE_USED'
    )
    print(message.sid)


def sendDMError(body_mess):
    message = client.messages.create(
        from_='whatsapp:+14155238886', 
        body=body_mess,
        # to='whatsapp:+14039985310'
        to='whatsapp:WHATSAPP_NUMBER_TO_BE_USED'
    )
    print(message.sid)


@app.route('/bot', methods=['GET', 'POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    message_details = incoming_msg.split(',')
    print(message_details)
    # message_details = ["2022", "Toyota", "Model Name 127XB", "29000", "12 Nov 2022"]
    image_url = image(message_details)
    print(image_url)
    print(incoming_msg)
    responded = False
    if len(message_details) == 5:
        sendDM("Here is your bill", image_url)
        responded = True
    if not responded:
        msg.body('Type error, sorry!')
        sendDMError("Reupload")

    return str(resp)


@app.route('/')
def home():
  return "BILL GENERATION STATUS: ONLINE"


def run():
  app.run(host='0.0.0.0', port=4000)


def keep_alive():
    t = Thread(target=run)
    t.start()


if __name__ == '__main__':
    app.run(port=4000)
