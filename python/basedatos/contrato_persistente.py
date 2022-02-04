import os
import pickle


class ContratoPersistente:

    def __init__(self):
        self._path = f'{os.path.dirname(os.path.abspath(__file__))}/temp/contratos'

    def guardar(self, contrato):
        file = f'{self._path}/{contrato.getCodigo()}'
        try:
            with open(file, 'wb') as f:
                pickle.dump(contrato, f, pickle.HIGHEST_PROTOCOL)
        except Exception:
            raise FileNotFoundError()

    def leer_uno(self, identificador):
        file = f'{self._path}/{identificador}'
        try:
            with open(file, 'rb') as f:
                contrato = pickle.load(f)
                return contrato
        except Exception:
            raise FileNotFoundError()

    def leer_todos(self):
        dir_path = f'{self._path}/'
        try:
            contratos = list(map(self.leer_uno, os.listdir(dir_path)))
            return contratos
        except Exception:
            raise FileNotFoundError()
