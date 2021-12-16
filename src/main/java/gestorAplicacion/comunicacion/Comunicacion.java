package gestorAplicacion.comunicacion;

import baseDatos.ClientePersistente;
import baseDatos.ContratoPersistente;
import gestorAplicacion.dominio.Cliente;
import gestorAplicacion.dominio.Contrato;
import gestorAplicacion.dominio.MedioComunicacion;

import java.util.List;

/**
 * MÓDULO CAPA LÓGICA
 *
 * Clase encargada de la comunicación del sistema.
 *
 * @author Juan Daniel Bula, Leidy Daniela Alzate, Oscar Andres Usuga
 */
public class Comunicacion {

    /** Constante para la notificación del mensaje */
    private static final String NOTIFICACION = "Mensaje '%s' enviado al %s %s";

    private final List<Cliente> clientes;
    private final List<Contrato> contratos;
    private final MedioComunicacion medioComunicacion;

    /**
     * Constructor sin parámetros que asigna todos los medios de comunicación existentes en el sistema.
     */
    public Comunicacion() {
        this(MedioComunicacion.TODOS);
    }

    /**
     * Constructor que asigna el medio de comunicación que está siendo pasado como parámetro.
     * @param medio medio de comunicación usado para el envío.
     */
    public Comunicacion(MedioComunicacion medio) {
        this.medioComunicacion = medio;
        this.clientes = leerClientes();
        this.contratos = leerContratos();
    }

    /**
     * Obtiene todos los clientes del sistema.
     * @return listado de clientes.
     */
    private List<Cliente> leerClientes() {
        ClientePersistente clientePersistente = new ClientePersistente();
        return clientePersistente.leerTodos();
    }

    /**
     * Obtiene todos los contratos del sistema.
     * @return listado de contratos.
     */
    private List<Contrato> leerContratos() {
        ContratoPersistente contratoPersistente = new ContratoPersistente();
        return contratoPersistente.leerTodos();
    }

    /**
     * Método encargado de enviar un mensaje a través de todos los medios de comunicación que existan.
     *
     * @param mensaje Mensaje que será enviado.
     */
    public void enviarMensaje(String mensaje) {
        enviarMensajeClientes(mensaje);
        enviarMensajeContratos(mensaje);
    }

    /**
     * Método que envía el mensaje por el medio de comunicación asignado a todos los clientes.
     * @param mensaje Mensaje a ser enviado
     */
    private void enviarMensajeClientes(String mensaje) {
        clientes.forEach(cliente -> {
            enviarMensaje(mensaje, "cliente", cliente.getNombre(), medioComunicacion);
        });
    }

    /**
     * Método que envía el mensaje por el medio de comunicación asignado a todos los contratos.
     * @param mensaje Mensaje a ser enviado.
     */
    private void enviarMensajeContratos(String mensaje) {
        contratos.forEach(contrato -> {
            enviarMensaje(mensaje, "contrato", contrato.getCodigo(), medioComunicacion);
        });
    }

    /**
     * Método encargado de enviar el mensaje usando los diferentes medios de comunicación existentes con implementación
     * particular según el medio escogido.
     * @param mensaje mensaje a ser enviado.
     * @param tipo tipo de entidad que lo recibe.
     * @param identificacion identificación de la entidad.
     * @param medioComunicacion medio usado.
     */
    private void enviarMensaje(String mensaje, String tipo, String identificacion, MedioComunicacion medioComunicacion) {
        String notificacion = String.format(NOTIFICACION, mensaje, tipo, identificacion);
        ServicioEnvio servicioEnvio;
        switch (medioComunicacion) {
            case EMAIL -> servicioEnvio = new ServicioEmail(notificacion);
            case SMS -> servicioEnvio = new ServicioSms(notificacion);
            case FAX -> servicioEnvio = new ServicioFax(notificacion);
            default -> servicioEnvio = new ServicioGenerico(notificacion);
        }
        servicioEnvio.enviar();
    }

    /**
     * Retorna todos los mensajes enviados a todos los clientes/contratos.
     * @return listado de mensajes enviados.
     */
    public List<String> obtenerMensajesEnviados() {
        return ServicioEnvio.getMensajesEnviados();
    }
}
