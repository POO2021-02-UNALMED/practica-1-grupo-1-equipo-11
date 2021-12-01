package uiMain;

import baseDatos.BaseDatos;

/**
 * MÓDULO UIMAIN
 *
 * Clase principal de la aplicación que ejecuta las funciones necesarias al momento de iniciar y finalizar la aplicación.
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
public class Aplicacion {

    public static void main(String[] args) {
        BaseDatos.iniciarObjetos();
        Menu.presentarMenuPrincipal();
        BaseDatos.persistirInformacion();
    }
}
