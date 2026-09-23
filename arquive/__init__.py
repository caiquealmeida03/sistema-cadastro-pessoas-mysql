from os import getenv
import mysql.connector
from mysql.connector import cursor
from time import sleep
from dotenv import load_dotenv

load_dotenv()

conexao = mysql.connector.connect(
    host=getenv("DB_HOST"),
    user=getenv('DB_USER'),
    password=getenv('DB_PASSWORD'),
    database=getenv('DB_NAME')
)

def mostrarArquivo():
    sleep(1)
    try:
        cursor = conexao.cursor()
        comando = f'SELECT * FROM lala'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        print(resultado)

    except:
        print('Não tem nenhum dado')
    else:
        print('Aqui estão os dados')

def atualizar():
    sleep(1)
    try:
        cursor = conexao.cursor()
        opc = str(input('O que deseja alterar? [nome] [nascimento] [sexo] [peso] [nacionalidade]')).upper()
        if opc == 'NOME' or opc == 'NASCIMENTO' or opc == 'SEXO' or opc == 'NACIONALIDADE':
            alt = str(input('Alteração: '))
        elif opc == 'PESO':
            alt = float(input('Alteração: '))
        n = int(input('Qual o id desejas alterar? '))

        comando = f'UPDATE lala SET {opc} = "{alt}" WHERE id = {n}'
        cursor.execute(comando)
        conexao.commit()
    except:
        print('Houve um erro ao tentar atualizar um dado')

    else:
        print('Alteração feita com sucesso')

def cadastrar():
    from interface import leiaInt
    sleep(1)
    try:
        a = conexao.cursor()
        nome = str(input('Nome: '))
        nasc = str(input('nascimento (xx/xx/xxxx): '))
        sex = str(input('Sexo [M/F]: '))
        peso = int(input('Peso: '))
        naciona = str(input('Nacionalidade: '))
        comando = f'INSERT INTO lala (nome,nascimento,sexo,peso,nacionalidade) VALUES("{nome}","{nasc}","{sex}",{peso},"{naciona}")'
        a.execute(comando)
        conexao.commit()
    except:
        print('Houve um problema para cadastrar seus dados')
    else:
        print('Dados cadastrados com sucesso')

def excluir():
    sleep(1)
    try:
        a = conexao.cursor()
        idp = int(input('Qual id desejas excluir? '))
        comando = f'DELETE FROM lala WHERE id = {idp}'
        a.execute(comando)
        conexao.commit()
    except Exception as erro:
        print(f'Houve um erro : {erro}')
    else:
        print('Dados excluídos com sucesso')
