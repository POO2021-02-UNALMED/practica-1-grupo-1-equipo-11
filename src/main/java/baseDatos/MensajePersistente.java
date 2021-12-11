package baseDatos;

import gestorAplicacion.dominio.Mensaje;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.List;

/**
 * Clase que implementa los métodos de la interfaz persistente para la persistencia de datos.
 *
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
public class MensajePersistente implements Persistente<Mensaje> {

    @Override
    public List<Mensaje> leerTodos() {
        return null;
    }

    @Override
    public void guardar(Mensaje mensaje) {
        FileOutputStream fo;
        try {
            fo = new FileOutputStream(System.getProperty("user.dir") + "\\src\\main\\java\\baseDatos\\temp\\mensajes.txt", true);
            ObjectOutputStream out = new ObjectOutputStream(fo);
            out.writeObject(mensaje);
            out.close();
            fo.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}