from enum import IntEnum


class Tipo(IntEnum):
    BURACO = 1
    ENTULHO = 2
    FAIXA_PEDESTRE = 3
    POSTE = 4
    DESNIVEL = 5


class Ocorrencia:
    def __init__(self, lat: float, longt: float, date: int, tipo: Tipo):
        self.lat: float = lat
        self.longt: float = longt
        self.date: int = date
        self.tipo: Tipo = tipo


class Usuario:
    def __init__(self, nome_usuario: str, nome: str, senha: str, salt: str):
        self.nome_usuario: str = nome_usuario
        self.nome: str = nome
        self.senha: str = senha
        self.salt: str = salt
