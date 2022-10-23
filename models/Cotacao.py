class Cotacao:

    def __init__(self, id: int = -1,  dolar: float = 0.0, euro: float = 0.0, data_hora: str = "") -> None:
        super().__init__()
        self.__id = id
        self.__dolar = dolar
        self.__euro = euro
        self.__data_hora = data_hora

    @property
    def id(self):
        return self.__id

    @property
    def dolar(self):
        return self.__dolar

    @property
    def euro(self):
        return self.__euro

    @property
    def data_hora(self):
        return self.__data_hora

    @property
    def cotacao(self) -> dict:
        return {
            'dolar': self.__dolar,
            'euro': self.__euro,
            'data_hora': self.__data_hora
        }

    def __str__(self) -> str:
        return f'{self.__data_hora}, $ {self.__dolar}, € {self.__euro}'