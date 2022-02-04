from gestoraplicacion.comunicacion.servicio_envio import ServicioEnvio


class ServicioEmail(ServicioEnvio):
    """
     Constructor asignando el mensaje al email.
     @param mensaje Mensaje a ser enviado.
    """
    def __init__(self, mensaje):
        super().__init__(mensaje)

    def enviar(self):
        super()._mensajes_enviados.append("EMAIL: " + super()._mensaje)