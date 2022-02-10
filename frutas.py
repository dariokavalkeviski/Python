#frutas.py

lista = []

def menu():
    opcao= -1
    print('\n\n\n#####Super Atacado de Frutas#####')
    print('Escolha:')
    print('1 = cadastrar')
    print('2 = listar')
    print('3 = remover')
    print('0 = sair')
    opcao = int(input('Qual opcao?'))

    while(opcao < 0 or opcao > 3):
        opcao = int(input('Qual opcao?'))
    return opcao

def cadastrar():
    quant = int(input('Quantas frutas voce quer cadastrar?'))
    for x in range(quant):
        fruta = input(f'Digite uma fruta {x + 1}')
        lista.append(fruta)

def remover():
    fruta = input('Qual fruta voce quer remover?')
    lista.remove(fruta)
    
escolha = -1

while escolha != 0:
    escolha = menu()

    if escolha == 1:
       cadastrar()
    elif escolha == 2:
        print('Frutas cadatrar = ', lista)
    elif escolha == 3:
        remover()


