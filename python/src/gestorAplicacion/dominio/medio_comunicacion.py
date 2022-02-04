from enum import Enum


class MedioComunicacion(Enum):
    EMAIL = 'email'
    SMS = 'sms'
    FAX = 'fax'
    TODOS = 'todos los medios'

    def __init__(self, valor):
        self.valor = valor

    def getValor(self):
        return self.valor