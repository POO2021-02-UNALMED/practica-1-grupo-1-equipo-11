package gestorAplicacion.dominio;

public enum MedioComunicacion {

    EMAIL("email"),
    SMS("sms"),
    FAX("fax"),
    TODOS("todos");

    private final String valor;

    MedioComunicacion(String valor) {
        this.valor = valor;
    }

    public String getValor() {
        return valor;
    }
}
