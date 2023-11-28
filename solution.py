class Vehiculo:
    def __init__(self, marca, modelo, año, precio, estado):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio
        self.estado = estado  # 'disponible' o 'vendido'

class Concesionaria:
    def __init__(self):
        self.inventario = []

    def agregar_vehiculo(self, vehiculo):
        pass

    def buscar_vehiculo(self, marca, modelo, año):
        pass

    def actualizar_estado_venta(self, vehiculo, nuevo_estado):
        pass
