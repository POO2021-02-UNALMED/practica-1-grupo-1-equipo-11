package baseDatos;

import gestorAplicacion.dominio.Contrato;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.List;

/**
 * Clase que implementa la interfaz Persistente para manejar la escritura y lectura de contratos en archivos.
 *
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
public class ContratoPersistente implements Persistente<Contrato> {

    @Override
    public void guardar(Contrato contrato) {
        FileOutputStream fos;
        try {
            String ruta = System.getProperty("user.dir") + String.format("\\src\\main\\java\\baseDatos\\temp\\contratos\\%s.txt", contrato.getCodigo());
            File file = new File(ruta);
            file.createNewFile();
            fos = new FileOutputStream(file);
            ObjectOutputStream oos = new ObjectOutputStream(fos);
            oos.writeObject(contrato);
            oos.close();
            fos.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public Contrato leerUno(String identificador) {
        FileInputStream fis;
        try {
            String ruta = String.format("\\src\\main\\java\\baseDatos\\temp\\contratos\\%s.txt", identificador);
            fis = new FileInputStream(System.getProperty("user.dir") + ruta);
            ObjectInputStream ois = new ObjectInputStream(fis);
            Contrato contrato = (Contrato) ois.readObject();
            ois.close();
            fis.close();
            return contrato;
        } catch (IOException | ClassNotFoundException e) {
            return null;
        }
    }

    @Override
    public void actualizar(Contrato contrato) {
        FileOutputStream fos;
        try {
            String ruta = String.format("\\src\\main\\java\\baseDatos\\temp\\contratos\\%s.txt", contrato.getCodigo());
            fos = new FileOutputStream(System.getProperty("user.dir") + ruta);
            ObjectOutputStream objectOutputStream = new ObjectOutputStream(fos);
            objectOutputStream.writeObject(contrato);
            objectOutputStream.close();
            fos.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
