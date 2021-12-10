package gestorAplicacion.comunicacion;

/**
 * Implementación de un servicio de envío específico usando EMAIL.
 *
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
public class ServicioEmail extends ServicioEnvio {

    /**
     * Constructor asignando el mensaje al email.
     * @param mensaje Mensaje a ser enviado.
     */
    public ServicioEmail(String mensaje) {
        super(mensaje);
    }

    @Override
    public void enviar() {
        ServicioEnvio.mensajesEnviados.add("EMAIL: " + mensaje);
    }
}
