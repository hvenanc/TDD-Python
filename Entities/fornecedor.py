from usuario import Usuario


class Fornecedor(Usuario):
    def __init__(self, nome, nome_usuario, email, senha, cpf, data_nasc):
        super().__init__(nome, nome_usuario, email, senha)
        self.__cpf = cpf
        self.__data_nasc = data_nasc

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def data_nasc(self):
        return self.__data_nasc

    @data_nasc.setter
    def data_nasc(self, data_nasc):
        self.data_nasc = data_nasc
