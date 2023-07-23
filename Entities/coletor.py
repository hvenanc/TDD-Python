from Entities.usuario import Usuario


class Coletor(Usuario):
    def __init__(self, nome, nome_usuario, email, senha, cep, cnpj):
        super().__init__(nome, nome_usuario, email, senha)
        self.__cep = cep
        self.__cnpj = cnpj

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj
