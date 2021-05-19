from User import User
from pprint import pprint

def send_message(username, result):
    user = User()
    user.setClient()
    client = user.getClient()
    with client:
        client.loop.run_until_complete(client.send_message(
            username,
            result))
    pprint(result)
