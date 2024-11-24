import requests

api_key = '3pak3UPM.yaVHKvjZYoIXfdLyIVrIrXN2SYxrVoeO'

your_query = input('You question : ')

# headers

headers = {
    'Content-Type' : 'application/json',
    'Apikey' : f'Api-Key {api_key}'
}

data = {
    'payload' : your_query
}

url = 'https://payload.vextapp.com/hook/FAEY9024KP/catch/$(channel_token)'

response = requests.post(url, json=data, headers=headers)

print(response.text)