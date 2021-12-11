package uiMain;

import baseDatos.ClientePersistente;
import baseDatos.MensajePersistente;
import gestorAplicacion.comunicacion.Comunicacion;
import gestorAplicacion.dominio.Cliente;
import gestorAplicacion.dominio.MedioComunicacion;
import gestorAplicacion.dominio.Mensaje;

import java.util.List;
import java.util.Scanner;

/**
 * MÓDULO INTERFAZ DE USUARIO
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

    /**
     * Imprime las opciones del menú principal.
     */
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
        Scanner scanner = new Scanner(System.in);
        int opcion;
        do {
            System.out.println("""
                    Seleccione los productos para la venta, seleccione 0 cuando no desee más productos:
                    1. Nevera
                    2. Horno
                    3. Microondas
                    4. Olla arrocera
                    5. Licuadora
                    6. Computador
                    7. Celular
                    8. Tablet
                    9. Audifonos
                    10. Estufa""");
            opcion = scanner.nextInt();
        } while (opcion != 0);

        System.out.println("""
                Escriba la cédula del cliente:""");
        scanner.nextLine();
        String cedula = scanner.nextLine();

        ClientePersistente clientePersistente = new ClientePersistente();
        Cliente cliente = clientePersistente.leerUno(cedula);
        if (cliente == null) {
            System.out.println("""
                    El cliente no existe, ingrese la siguiente información para crearlo:
                    Nombre
                    Correo
                    Celular""");
            String nombre = scanner.nextLine();
            String correo = scanner.nextLine();
            String celular = scanner.nextLine();

            cliente = new Cliente(nombre, cedula, correo, celular);
            clientePersistente.guardar(cliente);
        }
        // TODO código para crear una venta y asociar el cliente
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
     * Muestra el menú específico para enviar información a todos los clientes y contratos.
     */
    private static void presentarMenuEnviarInformacionMasiva() {
        System.out.println("Escriba el mensaje que desea enviar a todos los clientes/contratos:");
        Scanner scanner = new Scanner(System.in);
        String mensaje = scanner.nextLine();
        System.out.println("""
                Seleccione el medio de comunicación a usar:
                1. EMAIL
                2. SMS
                3. FAX
                4. TODOS""");
        int medioComunicacion = scanner.nextInt();

        Comunicacion comunicacion;
        switch (medioComunicacion) {
            case 1 -> comunicacion = new Comunicacion(MedioComunicacion.EMAIL);
            case 2 -> comunicacion = new Comunicacion(MedioComunicacion.SMS);
            case 3 -> comunicacion = new Comunicacion(MedioComunicacion.FAX);
            default -> comunicacion = new Comunicacion();
        }
        comunicacion.enviarMensaje(mensaje);
        System.out.println("---------------- MENSAJE ENVIADO ----------------\n");
        List<String> mensajesEnviados = comunicacion.obtenerMensajesEnviados();
        List<Mensaje> mensajes = mensajesEnviados.stream().map(Mensaje::new).toList();

        MensajePersistente mensajePersistente = new MensajePersistente();
        mensajes.forEach(mensajePersistente::guardar);
    }
}
