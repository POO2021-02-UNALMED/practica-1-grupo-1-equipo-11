package gestorAplicacion.comunicacion;

/**
 * Implementación de un servicio de envío específico usando FAX.
 *
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
public class ServicioFax extends ServicioEnvio {

    /**
     * Constructor asignando el mensaje al FAX.
     * @param mensaje mensaje a ser enviado.
     */
    public ServicioFax(String mensaje) {
        super(mensaje);
    }

    @Override
    public void enviar() {
        ServicioEnvio.mensajesEnviados.add("FAX: " + mensaje);
    }
}
