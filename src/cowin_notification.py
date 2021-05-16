import requests
import sys
from pprint import pprint
from datetime import date

def contractor():
        # date
        today = date.today()

        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"

PARAMS = {
    'pincode': sys.argv[1],
    'date': today.strftime("%d-%m-%Y")
}

r = requests.get(url=URL, params=PARAMS, headers=headers)

data = r.json()


def parser(data):
    for center in data['centers']:
        for session in center['sessions']:
            if session['min_age_limit'] == 18:
                temp = {
                    'age': '18+',
                    'address': center['address'],
                    'availablity': session['available_capacity'],
                    'vaccine': session['vaccine']
                }
                return temp


# print(data['centers'][1])
for center in data['centers']:
    # print(center['address'])
    for session in center['sessions']:
        # and session['available_capacity']!=0:
        if session['min_age_limit'] == 18:
            temp = {
                'age': '18+',
                'address': center['address'],
                'availablity': session['available_capacity'],
                'vaccine': session['vaccine']
            }
            print("18+", center['address'],
                  session['available_capacity'], session['vaccine'])
        if session['min_age_limit'] == 45 and session['available_capacity'] != 0:
            print("45+", center['address'],
                  session['available_capacity'], session['vaccine'])
        # print(session['min_age_limit'], session['available_capacity'])

# pprint(data)


def output_manjeet(data):
    pass


def output_sudarshan(data):
    pass
