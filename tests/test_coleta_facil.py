from Service.service import Service
from Entities.coletor import Coletor
from Repository.repository import Repositorio


class TestClass:
    def test_cadastro_usuario_coletor_com_dados_validos(self):
        dados = Repositorio()
        user = Coletor("Henrique Venancio", "hvs", "hvs@poli.br", "Invalida@77", "51345530", "34999724000102")
        cadastro = Service(dados)

        esperado = "Usuário Coletor Cadastrado com Sucesso!"
        resultado = cadastro.cadastrar_usuario_coletor(user)

        assert esperado == resultado
