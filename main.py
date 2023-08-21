class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    def cambiarColor(self, color):
        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in colores:
            self.color = color


class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        cantidadAsientos = 0
        for objeto in self.asientos:
            if type(objeto) == Asiento:
                cantidadAsientos += 1
        return cantidadAsientos

    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for objeto in self.asientos:
                if objeto.registro != self.registro:
                    return ("Las piezas no son originales")
                else:
                    return ("Auto original")
        return ("Las piezas no son originales")


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        if tipo == "gasolina" or tipo == "electrico":
            self.tipo = tipo
