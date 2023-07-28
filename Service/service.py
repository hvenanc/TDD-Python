import re
from validate_docbr import CPF, CNPJ
from Entities.coletor import Coletor
from Entities.fornecedor import Fornecedor
from Repository.repository import Repositorio


class Service:

    def __init__(self, repositorio: Repositorio):
        self._repositorio = repositorio

    @staticmethod
    def valida_cep(cep):
        if len(cep) != 8:
            return False

    @staticmethod
    def validar_cnpj(cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)

    @staticmethod
    def validar_senha(senha):
        if len(senha) < 8 or len(senha) > 32:
            return True

    @staticmethod
    def validar_nome(nome):
        return nome != "" and len(nome) > 3

    @staticmethod
    def validar_email(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, email):
            return True

    @staticmethod
    def validar_cpf(cpf):
        validador = CPF()
        return validador.validate(cpf)

    @staticmethod
    def validar_data(data):
        padrao = r"[0-9]+/[0-9]+/[0-9][0-9][0-9][0-9]"
        if re.match(padrao, data):
            return True

    def cadastrar_usuario_coletor(self, usuario: Coletor):
        if not self.validar_cnpj(usuario.cnpj):
            raise Exception("CNPJ Inválido")
        elif self.valida_cep(usuario.cep):
            raise Exception("Cep Inválido")
        elif not self.validar_nome(usuario.nome):
            raise Exception("Nome Inválido")
        elif not self.validar_email(usuario.email):
            raise Exception("Email Inválido")
        elif self.validar_senha(usuario.senha):
            raise Exception("Formato de Senha Inválido")

        self._repositorio.inserir(usuario)
        return "Usuário Coletor Cadastrado com Sucesso!"

    def cadastrar_usuario_fornecedor(self, usuario: Fornecedor):
        if not self.validar_cpf(usuario.cpf):
            raise Exception("CPF Inválido")
        elif not self.validar_nome(usuario.nome):
            raise Exception("Nome Inválido")
        elif not self.validar_data(usuario.data_nasc):
            raise Exception("Data Inválida")
        elif not self.validar_email(usuario.email):
            raise Exception("Email Inválido")
        elif self.validar_senha(usuario.senha):
            raise Exception("Formato de Senha Inválido")
        self._repositorio.inserir(usuario)
        return "Usuário Coletor Fornecedor com Sucesso!"

    def listar_usuarios_coletores(self):
        return self._repositorio.listar_usuarios()
