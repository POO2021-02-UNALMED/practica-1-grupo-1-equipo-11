import os
import pickle


class ClientePersistente:

    def __init__(self):
        self._path = f'{os.path.dirname(os.path.abspath(__file__))}/temp/clientes'

    def guardar(self, cliente):
        file = f'{self._path}/{cliente.get_cedula()}'
        with open(file, 'wb') as f:
            pickle.dump(cliente, f, pickle.HIGHEST_PROTOCOL)

    def leer_uno(self, identificador):
        file = f'{self._path}/{identificador}'
        with open(file, 'rb') as f:
            cliente = pickle.load(f)
            return cliente

    def leer_todos(self):
        dir_path = f'{self._path}/'
        clientes = list(map(self.leer_uno, os.listdir(dir_path)))
        return clientes
