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
}