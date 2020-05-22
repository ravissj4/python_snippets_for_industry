import requests

ngrok_url = 'https://bcc9f4e1.ngrok.io'
endpoint = f'{ngrok_url}/box-office-mojo-scrapper'

r = requests.post(endpoint, json={})

print(r.json())
