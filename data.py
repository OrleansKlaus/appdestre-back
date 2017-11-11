from enum import IntEnum


class Ocorrencia:
    def __init__(self, lat, long, date, tipo):
        self.lat: float = lat
        self.long: float = long
        self.date: int = date
        self.tipo: Tipo = tipo


class Tipo(IntEnum):
    BURACO = 1
    ENTULHO = 2
    FAIXA_PEDESTRE = 3
    POSTE = 4
    DESNIVEL = 5
