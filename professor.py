from pessoa_fisica import PessoaFisica

class Professor(PessoaFisica):
    def __init__(self, nome, cpf, formacao, tipo_vinculo):
        super().__init__(nome, cpf)
        self.__formacao = formacao
        self.__vinculo = tipo_vinculo

    @property
    def formacao(self):
        return self.__formacao

    @property
    def vinculo(self):
        return self.__vinculo

    def __str__(self):
        return "Professor: "+super().nome+" | CPF: "+super().cpf+" | Formacao: "+self.__formacao+" | Vinculo: "+self.__vinculo