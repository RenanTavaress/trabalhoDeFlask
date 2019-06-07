class Pessoa(object):
    def __init__(self,nome,telefone,cpf,email):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setTelefone(self, telefone):
        self.telefone = telefone

    def getTelefone(self):
        return self.telefone

    def setCpf(self, cpf):
        self.cpf = cpf

    def getCpf(self):
        return self.cpf

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

class Funcionario(Pessoa):
    def __init__(self,nome,telefone,cpf,email,matricula,cargo):
        super().__init__(nome,telefone,cpf,email)
        self.matricula = matricula
        self.cargo = cargo
    