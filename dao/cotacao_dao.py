from abc import ABC, abstractmethod


class CotacaoDAO(ABC):

    @abstractmethod
    def adicionar(self, cliente):
        pass

    @abstractmethod
    def selecionar_cotacao(self, limit=10) -> list:
        pass

    @abstractmethod
    def excluir(self, id):
        pass

    @abstractmethod
    def buscar_cotacao_hoje(self):
        pass

    # SELECT DATE(data_hora_coleta) FROM Cotacao
    # WHERE DATE(data_hora_coleta) = date('2022-04-04 13:16:11.818143');

#    @abstractmethod
#    def pesquisar(self, id):
#        pass