package gestorAplicacion.dominio;

import java.io.Serial;
import java.io.Serializable;

/**
 * MÓDULO CAPA LÓGICA
 *
 * Clase que representa un mensaje enviado dentro del sistema.
 *
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
public class Mensaje implements Serializable {

    @Serial
    private static final long serialVersionUID = 1L;

    private final String mensaje;

    public Mensaje(String mensaje) {
        this.mensaje = mensaje;
    }
}