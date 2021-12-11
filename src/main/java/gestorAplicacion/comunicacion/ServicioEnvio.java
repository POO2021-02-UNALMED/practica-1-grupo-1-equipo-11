package gestorAplicacion.comunicacion;

import java.util.ArrayList;
import java.util.List;

/**
 * Clase que representa la abstracción de un servicio de envío de mensajes de una forma genérica que luego debe
 * implementarse según el tipo de medio de comunicación usado.
 *
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
abstract class ServicioEnvio {

    protected static List<String> mensajesEnviados = new ArrayList<>(); // TODO guardar esto en un archivo para que los mensajes enviados queden persistidos
    protected String mensaje;

    /**
     * Constructor que asigna el mensaje que será enviado.
     * @param mensaje mensaje a ser enviado.
     */
    ServicioEnvio(String mensaje) {
        this.mensaje = mensaje;
    }

    /**
     * Retorna los mensajes enviados por el servicio de envío.
     * @return listado de mensajes enviados.
     */
    public static List<String> getMensajesEnviados() {
        return mensajesEnviados;
    }

    /**
     * Método abstracto que simula el envío de un mensaje a cualquier medio de comunicación asignado.
     */
    abstract void enviar();
}
