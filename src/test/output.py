#!/home/sudarshan/Cowin-Notification/venv/bin/python

import munger, random, pprint
from User import User
from pprint import pprint
from caller import caller
from message import messages

schema = {
    'Sudarshan Choudhary': ['311022', '302013', '302012'],
    '@manjeettanwar1026': ['302012', '302013']
    }

user = User()
user.setClient()
client = user.getClient()

for username in schema.keys():
    #print(username)
    for pincode in schema[username]:
        #print(pincode)
        data = caller(pincode)
        #print(data)
        results = munger.parser(data)
        #print(results)
        for result in results:
            #print(result)
            if len(result)!=0 and result['availablity']>0:
                with client:
                    client.loop.run_until_complete(client.send_message(
                        username,
                        messages[random.randint(0, 4)]))

                    client.loop.run_until_complete(client.send_message(
                        username,
                        str(result)))
                pprint(result)
