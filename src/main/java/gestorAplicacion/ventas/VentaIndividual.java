package gestorAplicacion.ventas;

import gestorAplicacion.dominio.Cliente;

import java.io.Serial;
import java.io.Serializable;
import java.util.List;

/**
 * Clase que representa una venta individual en el sistema.
 *
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
public class VentaIndividual implements Serializable {

    @Serial
    private static final long serialVersionUID = 4L;

    private String codigoVenta;
    private Cliente cliente;
    private List<Producto> productos;
    private String estado;

    public VentaIndividual(String codigo, Cliente cliente, List<Producto> productos) {
        this.codigoVenta = codigo;
        this.cliente = cliente;
        this.productos = productos;
        this.estado = "PENDIENTE";
    }

    public void venderProductos() {
        this.estado = "FINALIZADA";
        this.productos.forEach(Producto::venderProducto);
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }

    public String getCodigoVenta() {
        return codigoVenta;
    }

    public List<Producto> getProductos() {
        return productos;
    }

    @Override
    public String toString() {
        return String.format("""
                Venta [
                    codigo = %s,
                    cliente = %s,
                    productos = %s,
                    estado = %s
                ]""", codigoVenta, cliente, productos, estado);
    }
}