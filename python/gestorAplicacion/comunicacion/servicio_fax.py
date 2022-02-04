from gestoraplicacion.comunicacion.servicio_envio import ServicioEnvio


class ServicioFax(ServicioEnvio):
    """
     Constructor asignando el mensaje al FAX.
     @param mensaje mensaje a ser enviado.
    """
    def __init__(self, mensaje):
        super().__init__(mensaje)

    def enviar(self):
        super()._mensajes_enviados.append("FAX: " + super()._mensaje)