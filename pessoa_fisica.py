class PessoaFisica():
    def __init__(self, nome_pessoa, numero_cpf):
        self.__nome = nome_pessoa
        self.__cpf = numero_cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf