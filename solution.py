from datetime import datetime, timedelta


class Cliente:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id


class Reserva:
    def __init__(self, cliente, fecha_inicio, fecha_fin):
        self.cliente = cliente
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    # Métodos a implementar


class FechaNoDisponibleError(Exception):
    pass


class SistemaReservas:
    def __init__(self):
        self.reservas = []
