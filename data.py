from enum import Enum

class Ocorrencia:
    def __init__(self):
        self.lat: float
        self.long: float
        self.date: int
        self.tipo: Tipo
    
class Tipo(Enum):
    BURACO = 1
    ENTULHO = 2
    FAIXA_PEDESTRE = 3
    POSTE = 4
    DESNIVEL = 5
