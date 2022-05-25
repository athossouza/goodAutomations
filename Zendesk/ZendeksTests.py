
import requests


credentials = 'athos.souza@empresa.com.br','xxxxxxxx'
session = requests.Session()
session.auth = credentials
zendesk = 'https://skasuporte1641910091.zendesk.com'

ticket_id = 104
url = f'{zendesk}/api/v2/tickets/{ticket_id}.json'
response = session.get(url)
if response.status_code != 200:
    print(f'Error with status code {response.status_code}')
    exit()
data = response.json()
ticket_info = data['ticket']
print(ticket_info['description'])


