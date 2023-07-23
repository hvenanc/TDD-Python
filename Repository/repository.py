class Repositorio:
    def __init__(self):
        self._banco_dados = []

    def inserir(self, usuario):
        self._banco_dados.append(usuario)

    def listar_usuarios(self):
        return self._banco_dados

    def remover_usuario(self, usuario):
        self._banco_dados.remove(usuario)

