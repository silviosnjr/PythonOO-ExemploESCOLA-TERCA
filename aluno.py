from pessoa_fisica import PessoaFisica

class Aluno(PessoaFisica):
    def __init__(self, nome, cpf, codigo_cgm, turma):
        super().__init__(nome, cpf)
        self.__cgm = codigo_cgm
        self.__turma = turma

    @property
    def cgm(self):
        return self.__cgm

    @property
    def turma(self):
        return  self.__turma

    def __str__(self):
        return "Aluno: "+super().nome+" | CPF: "+super().cpf+" | CGM: "+self.__cgm+" | Turma: "+self.__turma