#graficos.py

import turtle

#cria um dicionario de cores
cores = dict()

#       chave       valor
cores["vermelho"] = "red"
cores["verde"] = "green"
cores["azul"] = "blue"
cores["amarelo"] = "yellow"
cores["cinza"] = "gray"
cores["laranja"] = "laranja"
cores["purpura"] = "purple"
cores["branco"] = "white"
cores["preto"] = "black"
cores["marrom"] = "marrom"
cores["rosa"] = "pink"

#obtem todas as chaves do dicionário
#nome da cor em português)
chaves = cores.keys()

#imprime todas as cores
for cor in chaves:
    print(cor)

#espera o usuário digitar uma das cores
cor = input(">>Digite uma das cores acima: ").lower()

#espera o usuário escolher LINHA ou CIRCULO
print("\nQual tipo de gráfico você quer: LINHA ou CIRCULO")
tipo = input(">>Digite LINHA ou CIRCULO: ").lower()

#agurada digitar um número inteiro
lados = int(input("Quantos lados? (3 a 6): "))

#agurada digitar um número inteiro
voltas = int(input("Quantas voltas? (10 a 300): "))

#muda a cor da caneta
turtle.pencolor(cores[cor])

#muda a espessura da caneta
turtle.pensize(3)

#executa o loop para desenhar
#atenção: a janela gráfica aparece por tras das outras!
for x in range(voltas):
    #desenha linha
    if tipo == 'linha':
        turtle.forward(x * 5)
    #desenha circulo
    else:
        turtle.circle(x * 5)
    turtle.left(360 / lados)
