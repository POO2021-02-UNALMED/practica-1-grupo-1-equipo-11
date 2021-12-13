package gestorAplicacion.dominio;

import gestorAplicacion.ventas.Producto;

import java.io.Serializable;
import java.util.List;

/**
 * Clase que representa un contrato en el sistema.
 *
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
public class Contrato implements Serializable {

    private String codigo;
    private Cliente cliente;
    private List<Producto> productos;
    private String estado;
    private TipoContrato tipoContrato;

    public Contrato(String codigo, Cliente cliente, List<Producto> productos, TipoContrato tipoContrato) {
        this.codigo = codigo;
        this.cliente = cliente;
        this.productos = productos;
        this.tipoContrato = tipoContrato;
        this.estado = "EJECUTADO";
    }

    public String getCodigo() {
        return codigo;
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
