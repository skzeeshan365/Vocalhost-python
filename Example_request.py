import vocalhost

vocalhost.API_KEY = 'ff90d1d4-f9ef-4c15-a987-fcdea3a9d13c'

while True:
    message = input('Send a message: ')
    response = vocalhost.Request.send(message, receiver_id='3')
    print('received: ' + response.text)