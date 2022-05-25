import requests
import json
from time import sleep
import getpass


zendesk = 'https://seu_dominio.zendesk.com' # Dominio do Zendesk (trocar aqui caso precise direcionar o aplicativo para outro banco)
agentLightCode = 1900002776527 # Código do Agent Light (Altere aqui se o código mudar)
agentFullCode = 1900002776547 # Código de Agent Full "Stuff" que consome licença (altere aqui se o código mudar)
funcaoHeads = 1900002776567 # Código de Função atribuída aos Heads

def autenticador():
    print('Digite seus dados de login do Zendesk [{}]'.format(zendesk.rsplit('https://')[1]))
    email = input('Digite seu e-mail: ')
    senha = input('Digite sua senha: ')
    #senha = getpass.getpass('Digite sua senha: ')

    credentials = email, senha
    session = requests.Session()
    session.auth = credentials

    url = f'{zendesk}/api/v2/users/me.json'
    response = session.get(url)
    if response.status_code != 200:
        print(f'Aconteceu algo errado, código: {response.status_code}')
        input('Pressione qualquer tecla para sair...')
        exit()
    data = response.json()
    user_info = data['user']
    userNome = user_info['name']
    if user_info['email'] == 'invalid@example.com':
        print('Você digitou algo errado em seu login (anônimo)')
        input('Pressione qualquer tecla para sair...')
        exit()
    userNome = userNome.split()
    primeirNome = userNome[0]
    if user_info['custom_role_id'] == funcaoHeads:
        print('{} você está na função de HEAD, podemos continuar'.format(primeirNome))
    else:
        print('{} Você não está em uma função de HEAD, procure o Admin do Zendesk'.format(primeirNome))
        input('Pressione qualquer tecla para fechar..')
        exit()


autenticador()




credentials = 'athos.souza@ska.com.br', 'xxxxxx'
session = requests.Session()
session.auth = credentials

headers = {'content-type': 'application/json'}




# Agent a remover a licença
def removeTecnico():
    global outTecnico
    global user1url
    global user1Tipo
    global firstNameU1
    global user1Role_Type
    global temChamado
    global custom_role_id

    outTecnico = input('Digite o código do técnico que vai REMOVER a licença: ')

    user_id = outTecnico
    user1url = f'{zendesk}/api/v2/users/{user_id}'
    response = session.get(user1url)
    if response.status_code != 200:
        print(f'Aconteceu algo errado, código: {response.status_code}')
        input('Pressione qualquer tecla para sair...')
        exit()
    data = response.json()
    user_info = data['user']
    user1Tipo = user_info['role']
    userNome = user_info['name']
    firstName = userNome.split()
    firstNameU1 = firstName[0]
    user1Role_Type = user_info['role_type']
    custom_role_id = user_info['custom_role_id']

    if user_info['role_type'] == 1 and user_info['role'] == 'agent':
        lTipo = 'Light'
    elif user_info['role_type'] == 0 and user_info['role'] == 'agent':
        lTipo = 'Full'
    elif user_info['role'] == 'admin':
        lTipo = 'Adminstrador'
    else:
        lTipo = 'cliente'


    print('Selecionado: [ {} ] Função atual: [ {} {} ]'.format(userNome, user1Tipo, lTipo))

    # Verifica se tem algum chamado que não está Fechado
    urlTemCh = f'{zendesk}/api/v2/search.json?query=assignee:{user_id} status:new status:hold status:open status:pending status:solved'
    responseCh = session.get(urlTemCh)
    cham = responseCh.json()
    temChamado = cham['count']



# Agent a adicionar a licença
def inserirTecnico():
    global inTecnico
    global user2url
    global user2Tipo
    global firstNameU2
    global user2Role_Type

    inTecnico = input('Agora digite o código do técnico para ADICIONAR a licença: ')

    user_id = inTecnico
    user2url = f'{zendesk}/api/v2/users/{user_id}'
    response = session.get(user2url)
    if response.status_code != 200:
        print(f'Aconteceu algo errado, código: {response.status_code}')
        input('Pressione qualquer tecla para sair...')
        exit()
    data = response.json()
    user_info = data['user']
    user2Tipo = user_info['role']
    userNome = user_info['name']
    firstName = userNome.split()
    firstNameU2 = firstName[0]
    user2Role_Type = user_info['role_type']

    if user_info['role_type'] == 1:
        lTipo = 'Light'
    elif user_info['role_type'] == 0:
        lTipo = 'Full'
    else:
        lTipo = 'Cliente'

    print('Selecionado: [ {} ] Função atual: [ {} {} ]'.format(userNome, user2Tipo, lTipo))


# Realiza a troca da licença
def fazATroca():

    alteraUser1 = {"user": {"custom_role_id": agentLightCode, "role_type": "1"}}  # Remove lcença
    pyload = json.dumps(alteraUser1)
    r = requests.put(user1url, data=pyload, auth=credentials, headers=headers)

    print('Licença removida de {}'.format(firstNameU1))

    alteraUser2 = {"user": {"custom_role_id": agentFullCode, "role_type": "0"}}  # Adiciona licença
    pyload = json.dumps(alteraUser2)
    r = requests.put(user2url, data=pyload, auth=credentials, headers=headers)
    print('Licença adicionada para {}'.format(firstNameU2))

    sleep(1)

def saudacao(s1):
    tam = len(s1)
    if tam:
        print('+', '-' * tam, '+')
        print('|', s1, '|')
        print('+', '-' * tam, '+')


# Inicio do Programa Principal

while True:

    saudacao('Trocador de Licenças Zendesk SKA v0.1 28/05/2022 (By Athos)')


    removeTecnico()


    inserirTecnico()


    confimacao = input('Confirmar a troca [S/N]: ')


    if confimacao.upper() == 'S':

        # Valida iformações do usuário a remover a licença
        if user1Tipo == 'admin': # Se for Admin, não deixa remover a licença
            print('{} é {}, não é possível remover a licença.'.format(firstNameU1, user1Tipo))

        elif user1Tipo == 'end-user': # Se form cliente (end-user), não deixa remover licença, pois não tem
            print('{} é {}, não é possível remover a licença.'.format(firstNameU1, user1Tipo))

        elif user1Role_Type == 1: # Se for Agent Light, não deixa remover a licença, pois não tem.
            print('{} é Agent Light e não tem licença'.format(firstNameU1))

        elif temChamado != 0:
            print('{} tem {} chamados não fechados. Transfira esses chamados e tente novamente.'.format(firstNameU1, temChamado))

        elif custom_role_id == funcaoHeads:
            print('{} tem a função de HEAD e não pode ter a licença removida'.format(firstNameU1))


        # Verifica o usuário para adicionar a licença
        elif user2Tipo == 'end-user': # Se for cliente (end-user) não deixa receber licença
            print('{} é {}, não é possível adicionar a licença.'.format(firstNameU2, user2Tipo))

        elif user2Tipo == 'agent' and user2Role_Type == 0:
            print('{} já é Agent Full e não é possível fazer a troca'.format(firstNameU2))


        elif user1Tipo == 'agent' and user1Role_Type == 0:
            fazATroca()

        maisUm = input('Fazer mais uma troca de licença [S/N]: ')
        if maisUm.upper() == 'S':
            continue
        else:
            exit()


    else:
        input('Cancelando troca de licença... \n Pressione qualquer tecla para fechar.')


