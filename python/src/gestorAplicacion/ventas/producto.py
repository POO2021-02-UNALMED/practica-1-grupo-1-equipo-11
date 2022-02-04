class Producto:
    productos_vendidos = []

    def __init__(self, codigo, nombre, precio, cantidad):
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    def getCodigo(self):
        return self._codigo

    def getNombre(self):
        return self._nombre

    def getCantidad(self):
        return self._cantidad

    def setCantidad(self, cantidad):
        self._cantidad = cantidad

    def venderProducto(self):
        Producto.productos_vendidos.append(self)
        self._cantidad -= 1

    def __str__(self):
        return "Producto [codigo = %s, nombre = %s, precio = %f]" % (self._codigo, self._nombre, self._precio)
