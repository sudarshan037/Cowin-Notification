import munger, random, pprint
from User import User
from pprint import pprint
from caller import caller
from message import messages

schema = {
    'Sudarshan Choudhary': ['311022'],
    '@manjeettanwar1026': ['302012', '302013']
}

user = User()
user.setClient()
client = user.getClient()

for username in schema.keys():
    for pincode in schema[username]:
        data = caller(pincode)
        results = munger.parser(data)
        for result in results:
            if len(result)!=0 and result['availablity']>0:
                with client:
                    client.loop.run_until_complete(client.send_message(
                        username,
                        messages[random.randint(0, 4)]))

                    client.loop.run_until_complete(client.send_message(
                        username,
                        str(result)))
                pprint(result)
