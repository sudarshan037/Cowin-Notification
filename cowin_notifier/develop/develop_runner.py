import time
import traceback
from develop import munger
from develop.caller import caller
from develop.message import messages
from messenger import send_message

import logging

logging.basicConfig(filename="develop.log",
        format='%(asctime)s %(message)s',
        filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.info("start")
def runner(data, dump):
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
                                if round(time.time()-dump[username][result['center_id']], 2)>=120:
                                    send_message(username, str(result))
                            else:
                                dump[username][result['center_id']] = round(time.time(), 2)
                                print("dump:", dump)
                                send_message(username, str(result))
    except:
        traceback.print_exc()
