
import requests

credentials = 'athos.souza@ska.com.br', 'xxxxxxx'
session = requests.Session()
session.auth = credentials
zendesk = 'https://skasuporte.zendesk.com/'

ticket_id = 289441
url = f'{zendesk}/api/v2/tickets/{ticket_id}.json'
response = session.get(url)
if response.status_code != 200:
    print(f'Error with status code {response.status_code}')
    exit()
data = response.json()


