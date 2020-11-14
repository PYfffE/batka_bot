import os

secret = 'secret'

f = open(os.path.dirname(__file__) + '/../bot_secret')
secret = f.read()
f.close()

settings = {
    'token': secret,
    'bot': 'Batka',
    'id': 7777,
    'prefix': '#'
}
