class Produto:


    #função buitin
    def __init__(self, descicao, preco, quantidade, id=None):
        self.__id = id
        self.__descricao = descicao
        self.__preco = preco
        self.__quantidade = quantidade

    def __str__(self):
        return (f'Codigo: {self.id} \tDescricao: {self.descricao} \tPreco Unitario: {self.__preco} \tQuantidade: {self.__quantidade}')


    #define propriedades para acessar os atributos
    @property
    def id(self):
        return self.__id

    @property
    def descricao(self):
        return self.__descricao

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidade(self):
        return self.__quantidade

    @id.setter
    def id(self, id):
        self.__id = id

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade



