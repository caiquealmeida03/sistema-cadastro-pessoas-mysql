def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número válido')
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n

def linha(tm=42):
    return '-'*tm

def titulo(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lst):
    titulo('MENU PRINCIPAL')
    cont = 0
    for c in lst:
        cont+=1
        print(f'{cont} - {c}')
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc
