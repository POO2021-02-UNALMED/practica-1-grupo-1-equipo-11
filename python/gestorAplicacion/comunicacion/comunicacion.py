from gestoraplicacion.dominio.medio_comunicacion import MedioComunicacion
from basedatos.cliente_persistente import ClientePersistente
from basedatos.contrato_persistente import ContratoPersistente
from gestoraplicacion.comunicacion.servicio_envio import ServicioEnvio
from gestoraplicacion.comunicacion.servicio_fax import ServicioFax
from gestoraplicacion.comunicacion.servicio_sms import ServicioSms
from gestoraplicacion.comunicacion.servicio_email import ServicioEmail
from gestoraplicacion.comunicacion.servicio_generico import ServicioGenerico


class Comunicacion:
    NOTIFICACION = 'Mensaje {} enviado al {} {}'

    def __init__(self, medio_comunicacion: MedioComunicacion.TODOS):
        self._medio_comunicacion = medio_comunicacion
        self._clientes = self.leerClientes()
        self._contratos = self.leerContratos()

    """
      Obtiene todos los clientes del sistema.
      @return listado de clientes.
    """
    def leerClientes(self):
        cliente_persistente = ClientePersistente()
        return cliente_persistente.leer_todos()

    """
      Obtiene todos los contratos del sistema.
      @return listado de contratos.
    """
    def leerContratos(self):
        contrato_persistente = ContratoPersistente()
        return contrato_persistente.leer_todos()

    """
     Método encargado de enviar un mensaje a través de todos los medios de comunicación que existan.
     @param mensaje Mensaje que será enviado.
    """
    def enviarMensajeTodos(self, mensaje):
        self.enviarMensajeClientes(mensaje)
        self.enviarMensajeContratos(mensaje)

    """
     Método que envía el mensaje por el medio de comunicación asignado a todos los clientes.
     @param mensaje Mensaje a ser enviado
    """
    def enviarMensajeClientes(self, mensaje):
        for cliente in self._clientes:
            Comunicacion.enviarMensaje(mensaje, "cliente", cliente.getNombre(), self._medio_comunicacion)

    """
      Método que envía el mensaje por el medio de comunicación asignado a todos los contratos.
      @param mensaje Mensaje a ser enviado.
    """
    def enviarMensajeContratos(self, mensaje):
        for contrato in self._contratos:
            Comunicacion.enviarMensaje(mensaje, "contrato", contrato.getCodigo(), self._medio_comunicacion)

    """
     Método encargado de enviar el mensaje usando los diferentes medios de comunicación existentes con implementación
      particular según el medio escogido.
      @param mensaje mensaje a ser enviado.
      @param tipo tipo de entidad que lo recibe.
      @param identificacion identificación de la entidad.
      @param medioComunicacion medio usado.
    """
    def enviarMensaje(self, mensaje, tipo, identificacion, medio_comunicacion):
        notificacion = Comunicacion.NOTIFICACION.format(mensaje, tipo, identificacion)
        servicio_envio = ServicioGenerico(notificacion)
        if medio_comunicacion == 'EMAIL':
            servicio_envio = ServicioEmail(notificacion)
        elif medio_comunicacion == 'SMS':
            servicio_envio = ServicioSms(notificacion)
        elif medio_comunicacion == 'FAX':
            servicio_envio = ServicioFax(notificacion)

        servicio_envio.enviar()

    """
     Retorna todos los mensajes enviados a todos los clientes/contratos.
     @return listado de mensajes enviados.
    """
    def obtenerMensajesEnviados(self):
        return ServicioEnvio.get_mensajes_enviados()