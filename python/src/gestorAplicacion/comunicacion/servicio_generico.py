from gestoraplicacion.comunicacion.servicio_email import ServicioEmail
from gestoraplicacion.comunicacion.servicio_envio import ServicioEnvio
from gestoraplicacion.comunicacion.servicio_fax import ServicioFax
from gestoraplicacion.comunicacion.servicio_sms import ServicioSms


class ServicioGenerico(ServicioEnvio):
    """
     Constructor asignando el mensaje a todos los medios.
     @param mensaje mensaje a ser enviado.
    """
    def __init__(self, mensaje):
        super().__init__(mensaje)

    def enviar(self):
        ServicioEmail(super()._mensaje).enviar()
        ServicioSms(super()._mensaje).enviar()
        ServicioFax(super()._mensaje).enviar()
