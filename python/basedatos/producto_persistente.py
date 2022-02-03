import os
import pickle


class ProductoPersistente:

    def __init__(self):
        self._path = f'{os.path.dirname(os.path.abspath(__file__))}/temp/productos'

    def guardar(self, producto):
        file = f'{self._path}/{producto.get_codigo()}'
        with open(file, 'wb') as f:
            pickle.dump(producto, f, pickle.HIGHEST_PROTOCOL)

    def leer_uno(self, identificador):
        file = f'{self._path}/{identificador}'
        with open(file, 'rb') as f:
            producto = pickle.load(f)
            return producto
