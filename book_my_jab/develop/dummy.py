import requests

url = "https://cdn-api.co-vin.in/api/v2/auth/public/generateOTP"

payload="{\n    \"mobile\": \"8946998793\"\n}"
headers = {
  'Content-Type': 'application/json',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

