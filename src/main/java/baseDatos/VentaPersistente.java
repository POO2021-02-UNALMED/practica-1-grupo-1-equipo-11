package baseDatos;

import gestorAplicacion.ventas.VentaIndividual;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.List;

/**
 * Clase que implementa la interfaz Persistente para manejar la escritura y lectura de las ventas en archivos.
 *
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
public class VentaPersistente implements Persistente<VentaIndividual> {

    @Override
    public List<VentaIndividual> leerTodos() {
        return null;
    }

    @Override
    public void guardar(VentaIndividual ventaIndividual) {
        FileOutputStream fos;
        try {
            String ruta = System.getProperty("user.dir") + String.format("\\src\\main\\java\\baseDatos\\temp\\ventas\\%s.txt", ventaIndividual.getCodigoVenta());
            File file = new File(ruta);
            file.createNewFile();
            fos = new FileOutputStream(file);
            ObjectOutputStream oos = new ObjectOutputStream(fos);
            oos.writeObject(ventaIndividual);
            oos.close();
            fos.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public VentaIndividual leerUno(String identificador) {
        return null;
    }

    @Override
    public void actualizar(VentaIndividual ventaIndividual) {

    }
}