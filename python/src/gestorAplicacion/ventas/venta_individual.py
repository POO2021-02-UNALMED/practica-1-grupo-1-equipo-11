class VentaIndividual:

    def __init__(self, codigo_venta, cliente, productos):
        self._estado = "PENDIENTE"
        self._codigo_venta = codigo_venta
        self._ciente = cliente
        self._productos = productos

    def venderProductos(self):
        self._estado = "FINALIZADA"
        for producto in self._productos:
            producto.venderProducto(producto)

    def devolverProducto(self, codigo_producto):
        for producto in self._productos:
            if codigo_producto == producto.getCodigo():
                self._productos.remove(producto)

        if self._productos is None:
            self.setEstado("DEVUELTA")

    def getEstado(self):
        return self._estado

    def setEstado(self, estado):
        self._estado = estado

    def getCodigoVenta(self):
        return self._codigo_venta

    def getProductos(self):
        return self._productos

    def __str__(self):
        return """"Venta [
        codigo = %s,
        cliente = %s
        productos = %s
        estado = %s
        ]""" % (self._codigo_venta, self._ciente, self._productos, self._estado)
