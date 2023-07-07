import vocalhost
import json

vocalhost.API_KEY = 'ff90d1d4-f9ef-4c15-a987-fcdea3a9d13c'

def generate_response(message):
    message = json.loads(message)
    print('received: ' + message.get('message'))
    message = input('Send a message: ')
    return message

vocalhost.process_message = generate_response

vocalhost.Receiver.connect(client_id='3')