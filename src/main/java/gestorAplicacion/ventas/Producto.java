package gestorAplicacion.ventas;

import java.io.Serial;
import java.io.Serializable;
import java.util.List;

/**
 * Clase que representa un producto dentro del sistema para la venta.
 *
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
public class Producto implements Serializable {

    @Serial
    private static final long serialVersionUID = 3L;
    private static List<Producto> productosVendidos;

    private String codigo;
    private String nombre;
    private double precio;
    private LineaProducto linea;
    private int cantidad;

    public Producto(String codigo, String nombre, double precio, int cantidad) {
        this.codigo = codigo;
        this.nombre = nombre;
        this.precio = precio;
        this.cantidad = cantidad;
    }

    public Producto(String codigo, String nombre, double precio, LineaProducto linea, int cantidad) {
        this(codigo, nombre, precio, cantidad);
        this.linea = linea;
    }

    public String getCodigo() {
        return codigo;
    }
}