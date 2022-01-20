#estoque.py


produto = input('Digite o nome do produto:')
preco = float(input('Digite o preco:'))
quantidade = int(input('Digite a quantidade: '))
total = quantidade * preco

#informar produto, prço e quantidade
print('Nome do produto:' , produto)
print('Preco do produto R$', preco)
print('Quantidade do produto:', quantidade)
print('Total do estoque R$ %.2f' % total)



      

