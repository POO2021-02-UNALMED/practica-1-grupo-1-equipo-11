import os
import pickle


class VentaPersistente:

    def __init__(self):
        self._path = f'{os.path.dirname(os.path.abspath(__file__))}/temp/ventas'

    def guardar(self, venta):
        file = f'{self._path}/{venta.get_codigo_venta()}'
        try:
            with open(file, 'wb') as f:
                pickle.dump(venta, f, pickle.HIGHEST_PROTOCOL)
        except Exception:
            raise FileNotFoundError()

    def leer_uno(self, identificador):
        file = f'{self._path}/{identificador}'
        try:
            with open(file, 'rb') as f:
                venta = pickle.load(f)
                return venta
        except Exception:
            raise FileNotFoundError()
