from enum import Enum

class TipoAnimal(Enum):
    VERTEBRADO = "vertebrado"
    INVERTEBRADO = "invertebrado"

class Animal:
    def __init__(self, cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo

    def comer(self):
        return "estoy comiendo"

class Perro(Animal):
    def __init__(self, nombre, raza, cantidad_patas, tipo):
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza

    def correr(self):
        return "estoy corriendo"

perro1 = Perro("Pancho", "Salchicha", 4, TipoAnimal.VERTEBRADO.value)
print(perro1.raza)
print(perro1.correr())
print(perro1.comer())
print(perro1.cantidad_patas)

class Aguila(Animal):
    def volar(self):
        return "estoy volando"

aguila1 = Aguila(2, TipoAnimal.VERTEBRADO.value)
print(aguila1.tipo)
print(aguila1.volar())
print(aguila1.comer())
print(aguila1.cantidad_patas)
