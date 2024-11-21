
# #lesson 12
# import requests
# import pandas as pd

# # URL = f"https://www.googleapis.com/oauth2/v3/userinfo"
# # token= ""
# # headers_param = {"Authorization": f"Bearer {token}"}
# # r = requests.get(url=URL, headers=headers_param)
# # result = r.json()


# # URL = f"https://robotfastapi.digitalberd.com/"
# # r = requests.get(url=URL)
# # result = r.json()
# #
# # if r.status_code == 200:
# #     print(result)
# #     print(type(result))
# #     print(r.text)
# #     print(r.status_code)
# #     print(result.get('data'))
# # else:
# #     print('was error')
# #     print(r.status_code)
# #     print(r.text)


# api_key = '1bbd0e4feae573037172783bf5a5ac2b'
# curr = 'RUB,GBP,EUR'
# start_date = '2024-11-20'
# end_date = '2024-11-21'
# URL = f'http://api.currencylayer.com/change?access_key={api_key}&currencies={curr}&start_date={start_date}&end_date={end_date}'
# r = requests.get(url=URL)
# result = r.json()
# print(result)
# print(result.get('quotes').get('USDRUB'))

# df1 = pd.DataFrame([result.get('quotes').get('USDRUB')])
# df1.to_csv("USDRUB.csv", index=False)
# df2 = pd.read_csv("USDRUB.csv")
# print(df2)

#lesson 13
import requests
import json

# Set up the URL
url = 'http://45.135.233.242:8001/to_insert'

# Set up the headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer your_token'
}

# Set up the request body
payload = {
    'symbol': '125'
}
json_payload = json.dumps(payload)
print(payload)

# Make the POST request
response = requests.post(url=url, params=payload)
print(response)
# Check the response
if response.status_code == 200:
    print('Request successful!')
    print(response.json())
else:
    print('Request failed!')
    print(response.text)