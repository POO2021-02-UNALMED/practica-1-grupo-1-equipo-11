package baseDatos;

import gestorAplicacion.dominio.Cliente;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.List;

/**
 * Clase que implementa la interfaz Persistente para manejar la escritura y lectura de clientes en archivos.
 *
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
public class ClientePersistente implements Persistente<Cliente> {

    @Override
    public List<Cliente> leerTodos() {
        return null; // TODO
    }

    @Override
    public void guardar(Cliente cliente) {

    }

    @Override
    public Cliente leerUno(String identificador) {
        FileInputStream fis;
        try {
            String ruta = String.format("/src/main/java/baseDatos/temp/clientes/%s.txt", identificador);
            fis = new FileInputStream(System.getProperty("user.dir") + ruta);
            ObjectInputStream ois = new ObjectInputStream(fis);
            return (Cliente) ois.readObject();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        return null;
    }
}