class Usuario:
    def __init__(self, nome, nome_usuario, email, senha):
        self.__nome = nome
        self.__nome_usuario = nome_usuario
        self.__email = email
        self.__senha = senha

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def nome_usuario(self):
        return self.__nome_usuario

    @nome_usuario.setter
    def nome_usuario(self, nome_usuario):
        self.__nome_usuario = nome_usuario

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha
