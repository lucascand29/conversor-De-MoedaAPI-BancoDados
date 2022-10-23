from abc import ABC, abstractmethod

class DAOFactory(ABC):

    @abstractmethod
    def dao_factory(self):
        pass

    @abstractmethod
    def cotacao_dao(self):
        pass