class Vehiculo:
    def __init__(self, marca: str, modelo: str, año: int, precio: float, estado: str):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio
        self.estado = estado  # 'disponible' o 'vendido'


class Concesionaria:
    def __init__(self):
        self.inventario = []

    def agregar_vehiculo(self, vehiculo: Vehiculo):
        pass

    def buscar_vehiculo(self, marca: str, modelo: str, año: int):
        pass

    def actualizar_estado_venta(self, vehiculo: Vehiculo, nuevo_estado: str):
        pass
