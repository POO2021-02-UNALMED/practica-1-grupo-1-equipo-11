package uiMain;

import java.util.Scanner;

/**
 * MÓDULO IUMAIN
 *
 * Presenta el menú principal de la aplicación, lee las opciones ingresadas por el usuario y delega la ejecución a los
 * métodos correspondientes.
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
public class Menu {

    /**
     * Muestra el menú principal de la aplicación con un mensaje de bienvenida.
     */
    public static void presentarMenuPrincipal() {
        presentarOpciones();
        Scanner scanner = new Scanner(System.in);
        int opcion = scanner.nextInt();
        while (opcion != 0) {
            switch (opcion) {
                case 1 -> presentarMenuRealizarVenta();
                case 2 -> presentarMenuRealizarDevolucion();
                case 3 -> presentarMenuEjecutarContrato();
                case 4 -> presentarMenuFinalizarContrato();
                case 5 -> presentarMenuEnviarInformacionMasiva();
                default -> System.out.println("---------------- OPCIÓN INCORRECTA ----------------");
            }
            presentarOpciones();
            opcion = scanner.nextInt();
        }
        System.out.println("---------------- GRACIAS, HASTA PRONTO ----------------");
    }

    private static void presentarOpciones() {
        System.out.println("""
                ---------------- BIENVENIDO(A) A NUESTRO CRM ----------------
        
                Por favor ingrese la operación que desea ejecutar:
                1. Realizar venta
                2. Realizar devolucion
                3. Ejecutar contrato de cliente
                4. Finalizar contrato de cliente
                5. Enviar información masiva
                0. Finalizar aplicación""");
    }

    /**
     * Muestra el menú específico para la creación de una venta.
     */
    private static void presentarMenuRealizarVenta() {
        // TODO
    }

    /**
     * Muestra el menú específico para ejecutar la devolución de una venta.
     */
    private static void presentarMenuRealizarDevolucion() {
        // TODO
    }

    /**
     * Muestra el menú específico para ejecutar un contrato con algún cliente.
     */
    private static void presentarMenuEjecutarContrato() {
        // TODO
    }

    /**
     * Muestra el menú específico para finalizar un contrato con algún cliente.
     */
    private static void presentarMenuFinalizarContrato() {
        // TODO
    }

    /**
     * Muestra el menú específico para enviar información a todos los clientes.
     */
    private static void presentarMenuEnviarInformacionMasiva() {
        System.out.println("Escriba el mensaje que desea enviar a todos los clientes:");
        String mensaje = new Scanner(System.in).nextLine();
//        Comunicacion.enviarInformacionMasiva(mensaje);
        System.out.println("---------------- MENSAJE ENVIADO ----------------\n");
    }
}
