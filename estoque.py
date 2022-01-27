#estoque

produtos=[ ]
quantidades = [ ]

def menu():
    opcao = -1
    while opcao != 0:
        print('########## Magazine da Maria ################')
        print('Sistema de Controle de Estoque - versão 1.0 #')
        print('Desenvolvido por: Dario                     #')
        print('1 = cadastrar')
        print('2 = listar')
        print('3 = Apagar')
        print('0 = sair')

        opcao = int(input('Qual opcao?'))

        if opcao == 1:
            cadastrar()

        elif opcao == 2:
            listar()

        elif opcao == 3:
            apagar()

        elif  opcao == 0:
            print('Saindo... Adeus!')

        else:
            print('Opcao nvalida')
    

def cadastrar():
    resp = 'S'
     
    while resp == 'S':

        nome = input('Digite o nome do produto: ')
        if nome in produtos:
            print('Produto já cadastrado!')
            continue

        #pede a quantidade e converte para inteiro
        quant = int(input('Digite a quantidade: '))
            
        #adiciona o produto na lista
        produtos.append(nome)

        #adiciona a quantidade na lista
        quantidades.append(quant)
        
        #'S' ou 'N'
        resp = input('Quer continuar? (S)im ou (N)ão: ').upper()

def listar():
    #mostra as lista
    print(produtos)
    print(quantidades)

def apagar():
    nome = input('Nome do produto para apagar do estoque:')
    #continua aqui na proxima aula

menu()

   

    
    


