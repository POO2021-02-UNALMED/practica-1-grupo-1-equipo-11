class Cliente:

    def __init__(self, nombre, cedula, correo, celular, contrato=None, medio_comunicacion=None):
        self._nombre = nombre
        self._cedula = cedula
        self._correo = correo
        self._celular = celular
        self._contrato = contrato
        self._medio_comunicacion = medio_comunicacion

    def getNombre(self):
        return self._nombre

    def getCedula(self):
        return self._cedula

    def getMedio_comunicacion(self):
        return self._medio_comunicacion

    def getContrato(self):
        return self._contrato

    def setContrato(self, contrato: object):
        self._contrato = contrato

    def __str__(self):
        return "Cliente [nombre = %s, cedula = %s]" % (self._nombre, self._cedula)
