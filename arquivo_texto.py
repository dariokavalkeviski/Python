#arquivo_texto.py

#modo para leitura e gravação de arquivos
#r = read = somente leitura
#w = write = escrita (perde oque já tem no arquivo)
#a = append = anexa dados (não perde)

#tipos de arquivos; texto ou binário

lista = []

def entrada():
    quant = int(input('Quantas frutas voce quer digitar?'))
    for x in range(1, quant +1):
        fruta = input('Digite a fruta {}:' .format(x))
        lista.append(fruta)

    print(lista)

def gravar():
    arquivo = open('frutas.txt', 'w')

    for fruta in lista:
        arquivo.write(fruta + '\n')

    arquivo.close()

def ler():
    arquivo = open('Frutas.txt', 'r')
    for linha in arquivo:
        print(linha)

    arquivo.close()

def anexar():
    arquivo = open('frutas.txt', 'a')
    for fruta in lista:
        arquivo.write(fruta + '\n')

    arquivo.close()

if (__name__ == '__main__'):
    entrada()
    #gravar()
    #ler()
    anexar()
    
