#arquivo_csv.py

#Permite gravar e ler arquivos em .csv do Excel

import csv

#Graavando um arquivo .csv

def gravar():
    tabela = (('PRODUTO', 'UNIDADE', 'PREÇO UNITÁRIO', 'QUANTIDADE DE ESTOQUE', 'VALOR TOTAL'),
                  ('Açucar', '2 Kg', 3.59, 10, 35.90),
                  ('Biscoito', '200 Gr', 1.19, 10, 11.90)
                 )

    #Cria um objeto de escrita
    saida = csv.writer(open('tabela.csv', 'w', newline=''), delimiter=';')

    #Escreve as tuplas no arquivo
    saida.writerows(tabela)

#Lendo arquivo .csv
def ler():
    tabela = csv.reader(open('tabela.csv'))

    #para cada linha do arquivo, imprima
    for lista in tabela:
        print(lista[0].split(';')[0])

if (__name__ == '__main__'):
    #gravar()
    ler()
                        
