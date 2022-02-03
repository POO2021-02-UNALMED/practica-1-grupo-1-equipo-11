import os.path
import pickle


class MensajePersistente:

    def __init__(self):
        self._path = f'{os.path.dirname(os.path.abspath(__file__))}/temp/mensajes'

    def guardar(self, mensaje):
        file = f'{self._path}'
        with open(file, 'ab') as f:
            pickle.dump(mensaje, f, pickle.HIGHEST_PROTOCOL)
