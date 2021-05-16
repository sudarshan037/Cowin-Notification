import configparser
from telethon import TelegramClient

class User:
    api_id, api_hash, phone, username = (None, None, None, None)
    client = None

    def __init__(self):
        # Reading configs
        config = configparser.ConfigParser()
        config.read("../config.ini")

        # setting config values
        self.api_id = config['Telegram']['api_id']
        self.api_hash = str(config['Telegram']['api_hash'])
        self.phone = config['Telegram']['phone']
        self.username = config['Telegram']['username']

    def setClient(self):
        # Create the client and connect
        self.client = TelegramClient(
            self.username,
            self.api_id,
            self.api_hash
            )
        print("Client Created")

    def getClient(self):
        return self.client

# user = User()
# user.setClient()
# client = user.getClient()
# with client:
#     client.loop.run_until_complete(client.send_message('', 'blah'))