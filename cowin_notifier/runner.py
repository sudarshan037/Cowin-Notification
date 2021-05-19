import random
import time
import json
import argparse
import traceback
from pprint import pprint

from User import User


#argument parser
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--develop', help='use this to run development code', action='store_true')
parser.add_argument('-p', '--prod', help='user this to run producation code', action='store_true')
args = vars(parser.parse_args())


#data preparation
develop_data = {
        'Sudarshan Choudhary': {'311022'}
        }
prod_data = None
dump = {}

with open("data/data.json", "r") as datafile:
    prod_data = json.load(datafile)
    for user in prod_data.keys():
        develop_data['Sudarshan Choudhary'] = develop_data['Sudarshan Choudhary'].union(set(prod_data[user]))
        dump[user] = {}

def timediff(username, center_id):
    return round(time.time()-dump[username][center_id], 2)

def send_message(username, result):
    user = User()
    user.setClient()
    client = user.getClient()
    with client:
        client.loop.run_until_complete(client.send_message(
            username,
            result))
    pprint(result)

#runners
def develop_runner(data):
    from develop import munger
    from develop.caller import caller
    from develop.message import messages

    try:
        while(True):
            for username in data.keys():
                for pincode in data[username]:
                    details = caller(pincode)
                    time.sleep(1)
                    results = munger.parser(details)
                    for result in results:
                        if len(result)!=0 and result['availability']>=0:
                            if result['center_id'] in dump[username].keys():
                                if timediff(username, result['center_id'])>30:
                                    send_message(username, str(result))
                            else:
                                dump[username][result['center_id']] = time.time()
                                print("dump:", dump)
                                send_message(username, str(result))
    except:
        traceback.print_exc()
    

def prod_runner(data):
    from prod import munger
    from prod.caller import caller
    from prod.message import messages
    
    try:
        while(True):
            for username in data.keys():
                for pincode in data[username]:
                    details = caller(pincode)
                    time.sleep(1)
                    results = munger.parser(details)
                    for result in results:
                        if len(result)!=0 and result['availability']>0:
                            if result['center_id'] in dump[username].keys():
                                if timediff(username, result['center_id'])>300:
                                    send_message(username, str(result))
                            else:
                                dump[username][result['center_id']] = time.time()
                                print("dump:", dump)
                                send_message(username, str(result))
    except:
        traceback.print_exc()

if __name__=='__main__':
    if args['develop']:
        pprint(develop_data)
        develop_runner(develop_data)
    elif args['prod']:
        pprint(prod_data)
        prod_runner(prod_data)
    else:
        print("help: use --develop or --prod arguments")

#add logging
#listener for availability
