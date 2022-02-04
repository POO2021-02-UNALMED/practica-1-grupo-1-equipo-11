class Contrato:

    def __init__(self, codigo, tipo_contrato):
        self._codigo = codigo
        self._tipo_contrato = tipo_contrato
        self._cliente = None
        self._estado = None
        self._productos = []

    def getCodigo(self):
        return self._codigo

    def ejecutarContrato(self, cliente, productos):
        self._estado = "EJECUTADO"
        self._cliente = cliente
        self._productos = productos

    def deshacerContrato(self):
        self._estado = "FINALIZADO"
        self._cliente.setContrato(None)
        self._cliente = None
        self._productos = []

    def getEstado(self):
        return self._estado

    def getCliente(self):
        return self._cliente

    def __str__(self):
        return """"
                Contrato [
                    codigo = %s,
                    cliente = %s,
                    productos = %s,
                    estado = %s,
                    tipo = %s
                ]""" % (self._codigo, self._cliente, self._productos, self._estado, self._tipo_contrato)
