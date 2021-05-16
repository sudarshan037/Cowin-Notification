import message, caller, munger, random, pprint

pincodes = ('311022')

for pincode in pincodes:
    data = caller.caller(pincode)
    temp = munger.parser(data)
    if temp!=None and temp['availablity']>=0:
        #create client
        #send message
        pprint.pprint(temp)
        print(message.messages[random.randint(0, 4)])
    