#!/home/sudarshan/Cowin-Notification/venv/bin/python

import munger, random
from User import User
from pprint import pprint
from caller import caller
from message import messages
import time

schema = {
    'Sudarshan Choudhary': ['311022', '302013', '302012', '302003', '302004', '302020', '302017', '302033', '302018'],
    '@manjeettanwar1026': ['302012', '302013'],
    '@zedd5321': ['302013', '302003', '302004', '302020', '302017', '302033', '302018', '302012']
    }

user = User()
user.setClient()
client = user.getClient()

while(True):
    flag = False
    for username in schema.keys():
        for pincode in schema[username]:
            data = caller(pincode)
            results = munger.parser(data)
            for result in results:
                if len(result)!=0 and result['availablity']>0:
                    flag = True
                    with client:
                        #client.loop.run_until_complete(client.send_message(
                        #    username,
                        #    messages[random.randint(0, 4)]))
    
                        client.loop.run_until_complete(client.send_message(
                            username,
                            str(result)))
                    pprint(result)
    if flag:
        time.sleep(10)
    else:
        time.sleep(1)
