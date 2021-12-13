package gestorAplicacion.dominio;

/**
 * Enum que representa los medios de comunicación del sistema.
 *
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
public enum MedioComunicacion {

    EMAIL("email"),
    SMS("sms"),
    FAX("fax"),
    TODOS("todos los medios");

    private final String valor;

    MedioComunicacion(String valor) {
        this.valor = valor;
    }

    public String getValor() {
        return valor;
    }
}
