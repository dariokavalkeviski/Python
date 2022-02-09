

matriz = [
            [3, 2, 6],
            [3, 3, 8],
            [1, 2, 5]

         ]
#imprime a matriz uma linha por vez
for linha in matriz:
    print(linha)

lin = int(input('Numero da linha:'))
col = int(input('Numero da coluna:'))
print(matriz[lin][col])

