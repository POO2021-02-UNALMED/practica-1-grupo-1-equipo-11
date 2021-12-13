package gestorAplicacion.dominio;

import java.io.Serial;
import java.io.Serializable;

/**
 * Clase que representa un cliente dentro del sistema.
 *
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
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

    /**
     * Constructor para crear clientes con la información mínima necesaria.
     * @param nombre nombre del cliente.
     * @param cedula cédula del cliente.
     * @param correo correo electrónico.
     * @param celular número móvil.
     */
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

    public Contrato getContrato() {
        return contrato;
    }

    public void setContrato(Contrato contrato) {
        this.contrato = contrato;
    }

    @Override
    public String toString() {
        return String.format("Cliente [nombre = %s, cédula = %s]", nombre, cedula);
    }
}