package gestorAplicacion.dominio;

public class Cliente {

    private String nombre;
    private MedioComunicacion medioComunicacion;

    public Cliente(String nombre, MedioComunicacion medioComunicacion) {
        this.nombre = nombre;
        this.medioComunicacion = medioComunicacion;
    }

    public String getNombre() {
        return nombre;
    }

    public MedioComunicacion getMedioComunicacion() {
        return medioComunicacion;
    }
}
