from pprint import pprint
from datetime import date
import requests

def caller(pincode):
    # date
    today = date.today()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"

    PARAMS = {
        'pincode': pincode,
        'date': today.strftime("%d-%m-%Y")
    }

    r = requests.get(url=URL, params=PARAMS, headers=headers)
    try:
        data = r.json()
    except:
        data = {"centers": []}
    return data

#pprint(caller('302012'))
