import munger, random, pprint
from User import User
from pprint import pprint
from caller import caller
from message import messages

pincodes = ('302012', '302013')

for pincode in pincodes:
    data = caller(pincode)
    temp = munger.parser(data)
    if temp!=None and temp['availablity']>=0:
        user = User()
        user.setClient()
        client = user.getClient()
        with client:
            client.loop.run_until_complete(client.send_message(
                'me',
                messages[random.randint(0, 4)]))

            client.loop.run_until_complete(client.send_message(
                'me',
                str(temp)))
        pprint(temp)
