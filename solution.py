from pydantic import BaseModel
import pickle


class Producto(BaseModel):
    nombre: str
    categoria: str
    precio: float
    cantidad: int


class Inventario(BaseModel):
    productos: dict[str, Producto] = {}

    def añadir_producto(self, nombre: str, categoria: str, precio: float, cantidad: int):
        # Implementar
        pass

    def actualizar_stock(self, nombre: str, nueva_cantidad: int):
        # Implementar
        pass

    def guardar_datos(self):
        # Implementar
        pass

    def cargar_datos(self):
        # Implementar
        pass
