package gestorAplicacion.dominio;

import gestorAplicacion.ventas.Producto;

import java.io.Serial;
import java.io.Serializable;
import java.util.Collections;
import java.util.List;

/**
 * Clase que representa un contrato en el sistema.
 *
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
public class Contrato implements Serializable {

    @Serial
    private static final long serialVersionUID = 5L;

    private String codigo;
    private Cliente cliente;
    private List<Producto> productos;
    private String estado;
    private TipoContrato tipoContrato;

    public Contrato(String codigo, TipoContrato tipoContrato) {
        this.codigo = codigo;
        this.tipoContrato = tipoContrato;
    }

    public String getCodigo() {
        return codigo;
    }

    public void ejecutarContrato(Cliente cliente, List<Producto> productos) {
        this.estado = "EJECUTADO";
        this.cliente = cliente;
        this.productos = productos;
    }

    public void deshacerContrato() {
        this.estado = "FINALIZADO";
        this.cliente = null;
        this.productos = Collections.emptyList();
    }

    @Override
    public String toString() {
        return String.format("""
                Contrato [
                    codigo = %s,
                    cliente = %s,
                    productos = %s,
                    estado = %s,
                    tipo = %s
                ]""", codigo, cliente, productos, estado, tipoContrato);
    }
}