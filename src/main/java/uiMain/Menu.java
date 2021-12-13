package uiMain;

import baseDatos.ClientePersistente;
import baseDatos.ContratoPersistente;
import baseDatos.MensajePersistente;
import baseDatos.ProductoPersistente;
import baseDatos.VentaPersistente;
import gestorAplicacion.comunicacion.Comunicacion;
import gestorAplicacion.dominio.Cliente;
import gestorAplicacion.dominio.Contrato;
import gestorAplicacion.dominio.MedioComunicacion;
import gestorAplicacion.dominio.Mensaje;
import gestorAplicacion.dominio.TipoContrato;
import gestorAplicacion.ventas.Producto;
import gestorAplicacion.ventas.VentaIndividual;

import java.util.ArrayList;
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

        List<Producto> productosSeleccionados = new ArrayList<>();
        ProductoPersistente productoPersistente = new ProductoPersistente();
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
            switch (opcion) {
                case 1 -> productosSeleccionados.add(productoPersistente.leerUno("01"));
                case 2 -> productosSeleccionados.add(productoPersistente.leerUno("02"));
                case 3 -> productosSeleccionados.add(productoPersistente.leerUno("03"));
                case 4 -> productosSeleccionados.add(productoPersistente.leerUno("04"));
                case 5 -> productosSeleccionados.add(productoPersistente.leerUno("05"));
                case 6 -> productosSeleccionados.add(productoPersistente.leerUno("06"));
                case 7 -> productosSeleccionados.add(productoPersistente.leerUno("07"));
                case 8 -> productosSeleccionados.add(productoPersistente.leerUno("08"));
                case 9 -> productosSeleccionados.add(productoPersistente.leerUno("09"));
                case 10 -> productosSeleccionados.add(productoPersistente.leerUno("10"));
            }
        } while (opcion != 0);

        if (productosSeleccionados.isEmpty()) {
            System.out.println("----- NO SE PUEDE CREAR UNA VENTA SIN PRODUCTOS -----");
            return;
        }

        System.out.println("Escriba la cédula del cliente:");
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

        System.out.println("Escriba el código para la venta:");
        String codigoVenta = scanner.nextLine();

        VentaIndividual venta = new VentaIndividual(codigoVenta, cliente, productosSeleccionados);
        System.out.printf("---------- LA VENTA TIENE ESTADO %s----------%n", venta.getEstado());

        venta.venderProductos();
        System.out.printf("---------- LA VENTA TIENE ESTADO %s----------%n", venta.getEstado());

        new VentaPersistente().guardar(venta);

        // Aquí se actualiza el inventario de cada producto ya que al venderse se debe restar la cantidad vendida.
        List<Producto> productosVendidos = venta.getProductos();
        productosVendidos.forEach(productoPersistente::actualizar);
    }

    /**
     * Muestra el menú específico para ejecutar la devolución de una venta.
     */
    private static void presentarMenuRealizarDevolucion() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Escriba el código de la venta a devolver:");
        String codigoVenta = scanner.nextLine();

        VentaPersistente ventaPersistente = new VentaPersistente();
        VentaIndividual ventaIndividual = ventaPersistente.leerUno(codigoVenta);

        System.out.println("La venta que existe es la siguente:");
        System.out.println(ventaIndividual);

        ProductoPersistente productoPersistente = new ProductoPersistente();
        System.out.println("Escriba el código del producto que desea devolver:");
        String codigoProducto = scanner.nextLine();
        Producto producto = productoPersistente.leerUno(codigoProducto);

        int cantidad = (int) ventaIndividual.getProductos()
                .stream()
                .filter(p -> p.getCodigo().equals(codigoProducto))
                .count();
        ventaIndividual.devolverProducto(codigoProducto);
        ventaPersistente.actualizar(ventaIndividual);

        producto.setCantidad(producto.getCantidad() + cantidad);
        productoPersistente.actualizar(producto);

        ventaIndividual = ventaPersistente.leerUno(codigoVenta);
        System.out.println("Así quedó la venta después de la devolución:");
        System.out.println(ventaIndividual);
    }

    /**
     * Muestra el menú específico para ejecutar un contrato con algún cliente.
     */
    private static void presentarMenuEjecutarContrato() {
        System.out.println("Escriba la cédula del cliente para el contrato:");
        Scanner scanner = new Scanner(System.in);

        String cedula = scanner.nextLine();
        Cliente cliente = new ClientePersistente().leerUno(cedula);

        if (cliente.getContrato() != null) {
            System.out.println("------- EL CLIENTE YA TIENE UN CONTRATO ASOCIADO -------");
            return;
        }

        System.out.println("Escriba el código del contrato:");
        String codigoContrato = scanner.nextLine();

        List<Producto> productosContrato = new ArrayList<>();
        ProductoPersistente productoPersistente = new ProductoPersistente();
        int producto;
        do {
            System.out.println("""
                    Seleccione los productos para el contrato, escriba 0 cuando no desee más productos:
                    1. Nevera
                    2. Horno
                    3. Microondas
                    4. Olla arrocera
                    5. Licuadora""");
            producto = scanner.nextInt();
            switch (producto) {
                case 1 -> productosContrato.add(productoPersistente.leerUno("01"));
                case 2 -> productosContrato.add(productoPersistente.leerUno("02"));
                case 3 -> productosContrato.add(productoPersistente.leerUno("03"));
                case 4 -> productosContrato.add(productoPersistente.leerUno("04"));
                case 5 -> productosContrato.add(productoPersistente.leerUno("05"));
            }
        } while (producto != 0);

        System.out.println("""
                Seleccione el tipo de contrato:
                1. MAYORISTA
                2. MINORISTA""");
        int seleccion = scanner.nextInt();
        TipoContrato tipoContrato;
        if (seleccion == 1) {
            tipoContrato = TipoContrato.MAYORISTA;
        } else {
            tipoContrato = TipoContrato.MINORISTA;
        }

        Contrato contrato = new Contrato(codigoContrato, tipoContrato);
        contrato.ejecutarContrato(cliente, productosContrato);

        ContratoPersistente contratoPersistente = new ContratoPersistente();
        contratoPersistente.guardar(contrato);

        cliente.setContrato(contrato);
        new ClientePersistente().actualizar(cliente);

        Contrato contratoLeido = contratoPersistente.leerUno(codigoContrato);
        System.out.println("------- CONTRATO EJECUTADO -------");
        System.out.println(contratoLeido);
    }

    /**
     * Muestra el menú específico para finalizar un contrato con algún cliente.
     */
    private static void presentarMenuFinalizarContrato() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese el código del contrato a finalizar:");
        String codigoContrato = scanner.nextLine();

        ContratoPersistente contratoPersistente = new ContratoPersistente();
        Contrato contrato = contratoPersistente.leerUno(codigoContrato);

        System.out.println("Esta es la información del contrato a finalizar:");
        System.out.println(contrato);

        System.out.println("¿Está seguro? (Escriba s o n)");
        String respuesta = scanner.nextLine();
        if ("s".equalsIgnoreCase(respuesta)) {
            contrato.deshacerContrato();
            contratoPersistente.actualizar(contrato);
            System.out.println(" ------- EL CONTRATO HA SIDO FINALIZADO -------");
        } else {
            System.out.println(" ------- EL CONTRATO NO FUE FINALIZADO -------");
        }

        contrato = contratoPersistente.leerUno(codigoContrato);
        System.out.println("Esta es la información del contrato después de la operación:");
        System.out.println(contrato);
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
