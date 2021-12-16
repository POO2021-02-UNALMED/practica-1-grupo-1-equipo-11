package baseDatos;

import gestorAplicacion.dominio.Cliente;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * Clase que implementa la interfaz Persistente para manejar la escritura y lectura de clientes en archivos.
 *
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
public class ClientePersistente implements Persistente<Cliente> {

    @Override
    public List<Cliente> leerTodos() {
        try (Stream<Path> stream = Files.list(Paths.get(System.getProperty("user.dir") + "\\src\\main\\java\\baseDatos\\temp\\clientes"))) {
            List<String> files = stream
                    .filter(file -> !Files.isDirectory(file))
                    .map(Path::getFileName)
                    .map(fileName -> fileName.toString().replace(".txt", ""))
                    .toList();
            return files.stream()
                    .map(this::leerUno)
                    .collect(Collectors.toList());
        } catch (IOException e) {
            e.printStackTrace();
        }
        return Collections.emptyList();
    }

    @Override
    public void guardar(Cliente cliente) {
        FileOutputStream fos;
        try {
            String ruta = System.getProperty("user.dir") + String.format("\\src\\main\\java\\baseDatos\\temp\\clientes\\%s.txt", cliente.getCedula());
            File file = new File(ruta);
            file.createNewFile();
            fos = new FileOutputStream(file);
            ObjectOutputStream oos = new ObjectOutputStream(fos);
            oos.writeObject(cliente);
            oos.close();
            fos.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public Cliente leerUno(String identificador) {
        FileInputStream fis;
        try {
            String ruta = String.format("\\src\\main\\java\\baseDatos\\temp\\clientes\\%s.txt", identificador);
            fis = new FileInputStream(System.getProperty("user.dir") + ruta);
            ObjectInputStream ois = new ObjectInputStream(fis);
            Cliente cliente = (Cliente) ois.readObject();
            ois.close();
            fis.close();
            return cliente;
        } catch (IOException | ClassNotFoundException e) {
            return null;
        }
    }

    @Override
    public void actualizar(Cliente cliente) {
        FileOutputStream fos;
        try {
            String ruta = String.format("\\src\\main\\java\\baseDatos\\temp\\clientes\\%s.txt", cliente.getCedula());
            fos = new FileOutputStream(System.getProperty("user.dir") + ruta);
            ObjectOutputStream objectOutputStream = new ObjectOutputStream(fos);
            objectOutputStream.writeObject(cliente);
            objectOutputStream.close();
            fos.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}