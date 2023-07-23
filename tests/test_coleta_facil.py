from Service.service import Service
from Entities.coletor import Coletor
from Entities.fornecedor import Fornecedor
from Repository.repository import Repositorio


class TestClass:
    def test_cadastro_usuario_coletor_com_dados_validos(self):
        dados = Repositorio()
        user = Coletor("Henrique Venancio", "hvs", "hvs@poli.br", "Invalida@77", "51345530", "34999724000102")
        cadastro = Service(dados)

        esperado = "Usuário Coletor Cadastrado com Sucesso!"
        resultado = cadastro.cadastrar_usuario_coletor(user)

        assert esperado == resultado

    def test_cadastro_usuario_forncedor_com_dados_validos(self):
        dados = Repositorio()
        user = Fornecedor("Henrique", "hvs", "hvs@gmail.com", "Inva94005", "71724311034", "24/03/1985")
        cadastro = Service(dados)

        esperado = "Usuário Coletor Fornecedor com Sucesso!"
        resultado = cadastro.cadastrar_usuario_fornecedor(user)

        assert esperado == resultado
