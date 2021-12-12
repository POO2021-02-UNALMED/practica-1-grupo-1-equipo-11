package baseDatos;

import java.util.List;

/**
 * Interfaz que define los métodos necesarios para leer, escribir, actualizar y eliminar objetos.
 *
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
public interface Persistente<T> {

    /**
     * Método para leer todos los objetos especificados.
     * @return listado de objetos leídos.
     */
    List<T> leerTodos();

    /**
     * Método para guardar el objeto pasado como parámetro.
     * @param t objeto a ser guardado.
     */
    void guardar(T t);

    /**
     * Método para leer un objeto.
     * @param identificador clave primaria del objeto.
     * @return objeto leido.
     */
    T leerUno(String identificador);

    /**
     * Método para actualizar el objeto ingresado como parámetro.
     * @param t objeto a ser actualizado.
     */
    void actualizar(T t);
}