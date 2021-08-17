from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

class Escola :
    def __init__(self):
        self.__nome = "Escola dos Programadores de Python do Edutech"

        aluno1 = Aluno("Ciclano da Silva", "111.222.333-44", "0001", "3º B")
        aluno2 = Aluno("Bento José", "444.555.666-77", "0002", "1º A")
        professor1 = Professor("Beltrano da Silva", "999.999.999-99", "Geografia", "concursado")
        funcionario1 = Funcionario("Severino de Oliveira", "777.555.444-00", "Porteiro", "das 08h às 17h")

        self.__pessoas = [aluno1, aluno2, professor1, funcionario1]

    def __getitem__(self, item):
        return self.__pessoas[item]

    def __len__(self):
        return len(self.__pessoas)

    def solicitaAcesso(self):
        codigo_acesso = input("Digite seu código de acesso: ")
        for pessoa in self.__pessoas:
            if(pessoa.acessaEscola(codigo_acesso)):
                return True
        print("Acesso negado!")
        return False