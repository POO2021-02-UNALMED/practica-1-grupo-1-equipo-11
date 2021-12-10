package gestorAplicacion.comunicacion;

/**
 * Implementación de un servicio de envío específico usando SMS.
 *
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
public class ServicioSms extends ServicioEnvio {

    /**
     * Constructor asignando el mensaje al SMS.
     * @param mensaje mensaje a ser enviado.
     */
    public ServicioSms(String mensaje) {
        super(mensaje);
    }

    @Override
    public void enviar() {
        ServicioEnvio.mensajesEnviados.add("SMS: " + mensaje);
    }
}
