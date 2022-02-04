class ServicioEnvio:
    _mensajes_enviados = []
    """
     Constructor que asigna el mensaje que será enviado.
     @param mensaje mensaje a ser enviado.
    """
    def __init__(self, mensaje):
        self._mensaje = mensaje

    """
     Retorna los mensajes enviados por el servicio de envío.
     @return listado de mensajes enviados.
    """
    @staticmethod
    def get_mensajes_enviados():
        return ServicioEnvio._mensajes_enviados
