package gestorAplicacion.comunicacion;

/**
 * Implementación de un servicio de envío específico usando todos los medios.
 *
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
public class ServicioGenerico extends ServicioEnvio {

    /**
     * Constructor asignando el mensaje a todos los medios.
     * @param mensaje mensaje a ser enviado.
     */
    public ServicioGenerico(String mensaje) {
        super(mensaje);
    }

    @Override
    public void enviar() {
        new ServicioEmail(mensaje).enviar();
        new ServicioSms(mensaje).enviar();
        new ServicioFax(mensaje).enviar();
    }
}
