#adivinhação.py

import random

def jogar():
    print('********************************')
    print('Bem vindo ao jogo de adivinhação')
    print('********************************')

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print('Qual o nivel de dificuldade?')
    print('(1) Facil (2) Medio (3) Dificil')

    nivel = input('Defina o nivel:')

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5


    for tentativa in range (1, total_tentativas + 1):
        print(f' Tentativa {tentativa} de {total_tentativas}')
        chute = int(input('Digite um numero entre 1 e 100: '))

        if(chute == numero_secreto):
            print('Acertou')
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        if(chute > numero_secreto):
            print('Errou! Seu chute foi maior que o numero secrteo')
        else:
            print('Errou! Seu chute foi menor que o numero secreto')

    print('**Fim de jogo**')
    print(f'O numero era {numero_secreto}. Voce fez {pontos} pontos.')


if(__name__ == '__main__'):
    jogar()
        

        
        

