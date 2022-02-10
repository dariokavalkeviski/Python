#conta.py

class Conta:

  
    def __init__(self, numero, titular, saldo, limite):
        print('Construindo objeto... {}'.format(self))
        #atributos privados
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self, valor):
       self.__saldo += valor

    def sacar(self, valor):
          if(self.__saldo + self.__limite >= valor):
             self.__saldo -= valor
             return True
          else:
              print('Não há saldo suficiente para sacar')

    def transferir(self, valor, destino):
          if self.sacar(valor):
             destino.depositar(valor)
          else:
            print('Não há saldo para transferencia')

    @property
    def numero(self):
       return(self.__saldo)

    @property
    def titular(self):
       return(self.__titular)
    
    @property
    def saldo(self):
       return(self.__numero)

    @property
    def limite(self):
       return(self.__limite)

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    #exemplo de metodo estático
    @staticmethod
    def codigo_banco():
        return '001'
    
    
contaJoao = Conta(123, 'João da Silava', 100, 1000)
contaZe = Conta(456, 'José da Silva', 100, 1000)

contaJoao.transferir(500, contaZe)

print(contaZe.numero)
print(contaZe.titular)
print(contaZe.saldo)
print(contaZe.limite)
print(contaZe.saldo)
print(Conta.codigo_banco())
