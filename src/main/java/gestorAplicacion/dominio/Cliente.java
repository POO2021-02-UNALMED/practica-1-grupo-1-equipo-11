package gestorAplicacion.dominio;

import java.io.Serial;
import java.io.Serializable;

public class Cliente implements Serializable {

    @Serial
    private static final long serialVersionUID = 2L;

    private String nombre;
    private String cedula;
    private String correo;
    private String celular;
    private String pbx;
    private String estado;
    private Contrato contrato;
    private MedioComunicacion medioComunicacion;

    public Cliente(String nombre, String cedula, String correo, String celular) {
        this.nombre = nombre;
        this.cedula = cedula;
        this.correo = correo;
        this.celular = celular;
    }

    public Cliente(String nombre, MedioComunicacion medioComunicacion) {
        this.nombre = nombre;
        this.medioComunicacion = medioComunicacion;
    }

    public String getNombre() {
        return nombre;
    }

    public String getCedula() {
        return cedula;
    }

    public MedioComunicacion getMedioComunicacion() {
        return medioComunicacion;
    }
}