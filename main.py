from interface import*
from arquive import*


cursor = conexao.cursor()

while True:
    res = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa','Atualizar um dado','Excluir um dado', 'Sair do Sistema'])
    if res == 1:
        titulo('Opção 1')
        mostrarArquivo()
    elif res == 2:
        titulo('Opção 2')
        cadastrar()
    elif res == 3:
        titulo('Opção 3')
        atualizar()
    elif res == 4:
        titulo('Opção 4')
        excluir()
    elif res == 5:
        print('Saindo do Sistema... Até logo!')
        conexao.close()
        cursor.close()
        break
    else:
        print('ERRO! Digite uma opção válida')
