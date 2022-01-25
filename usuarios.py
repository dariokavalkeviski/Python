#login.pye

#Algoritimo
#1.criar uma lista com nomes de usuarios
#2.perguntar o nome do usuario
#3.verificar se o usuario e valido ou invalido


usuarios = ['Joao', 'Jose', 'Pedro', 'Maria', 'Antonio', 'Carlos',  'Sergio']
usuario = input('Digite o nome do usuario:').capitalize()

if usuario in usuarios:
    print('usuario logado')
else:
    print('usuario nao encontrado')
    





