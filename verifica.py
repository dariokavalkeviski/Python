#verifica.py

#Algoritimo
#1.cria uma lista de cores
#2.pergunta ao usuario o nome de uma cor
#3.diz para o usuario se a cor existe na lista
#4.Se nao ta na lista, adiciona (anexar = append) na lista

cores = ['verde', 'amarelo', 'azul', 'branco', 'preto', 'branco', 'vermelho', 'verde', 'azul', 'amarelo']
cor = input('digite nome de uma cor:')

if cor in cores:
    print('Ta na lista')
else:
    print('Nao ta na lista')

    cores.append(cor)

