import requests
from hashlib import sha256
from pprint import pprint


def generateOTP():
    url = "https://cdn-api.co-vin.in/api/v2/auth/public/generateOTP"
    payload = "{\n    \"mobile\": \"8946998793\"\n}"
    headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            }

    response = requests.request(
            method = "POST",
            url = url,
            headers = headers,
            data = payload)

    print(response.text)
    return response.json()['txnId']


def confirmOTP(txnId, OTP):
    OTP = sha256(OTP.encode('utf-8')).hexdigest()
    url = "https://cdn-api.co-vin.in/api/v2/auth/public/confirmOTP"
    payload= '{\n    \"otp\": \"'+OTP+'\",\n    \"txnId\": \"'+txnID+'\"\n}'
    headers = {
            'Content-Type': 'application/json',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
            }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    return response.json()['token']

def dummy():
    url = 'https://cdn-api.co-vin.in/api/v2/auth/generateMobileOTP'
    data = {
            "mobile": "8946998793",
            "secret": "U2FsdGVkX1+z/4Nr9nta+2DrVJSv7KS6VoQUSQ1ZXYDx/CJUkWxFYG6P3iM/VW+6jLQ9RDQVzp/RcZ8kbT41xw=="
            }
    headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            }
    txnId = requests.post(url=url, json=data, headers=headers)
    print(txnId.text)


#beneficiaries

txnId = generateOTP()
#token = confirmOTP(txnId)
#dummy()
