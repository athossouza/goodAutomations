import requests
import pandas as pd
from openpyxl import Workbook

def borda(s1):
    tam = len(s1)
    if tam:
        print('+', '-' * tam, '+')
        print('|', s1, '|')
        print('+', '-' * tam, '+')

borda('Zendesk Excel Export Organization Users v0.1 23/05/2022 (By Athos)')

print('É necessário um login de usuário Admin para exportar Excel do Zendesk')

email = input('Digite o e-mail: ')
senha = input('Digite a senha: ')
dominio = input('Digite o domínio [Ex.: "skasuporte"]: ')
empresa = input('Digite o código da Organization do Zendesk [Ex.: 361238136051 para SKA]: ')

print('Conectando...')

credentials = email , senha
session = requests.Session()
session.auth = credentials
zendesk = f'https://{dominio}.zendesk.com'


organization_id = empresa
users_name = []
url = f'{zendesk}/api/v2/organizations/{organization_id}/users.json'
while url:
    response = session.get(url)
    if response.status_code != 200:
        print(f'Error with status code {response.status_code}')
        input('Você digitou algo errado ou não é Admin do Zendesk')
        exit()
    data = response.json()
    users_name.extend(data['users'])
    url = data['next_page']

def exportExcel():
    print('Exportando...')
    users = pd.DataFrame(users_name, columns=['name', 'role','custom_role_id', 'default_group_id'])
    users.to_excel('UsuariosZD.xlsx', index=False)

exportExcel()

print('Arquivo "UsuariosZD.xlsx" exportado! ')
print('')
input('Pressione qualquer tecla para sair...')
