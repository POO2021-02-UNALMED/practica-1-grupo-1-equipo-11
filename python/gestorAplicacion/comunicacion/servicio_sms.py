from gestoraplicacion.comunicacion.servicio_envio import ServicioEnvio


class ServicioSms(ServicioEnvio):
    """
     Constructor asignando el mensaje al SMS.
     @param mensaje mensaje a ser enviado.
    """
    def __init__(self, mensaje):
        super().__init__(mensaje)

    def enviar(self):
        super()._mensajes_enviados.append("SMS: " + super()._mensaje)
