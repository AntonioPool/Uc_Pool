from dataclasses import dataclass

@dataclass
class Personaje:

    Nombre: str
    Vida: int
    Ataque: int
    Defensa: int
    Nivel: int

    def imprimir(self):
        print(self.Nombre,self.Vida, self.Ataque, self.Defensa, self.Nivel)
    


personaje = Personaje("Alan", 120, 15, 50, 10)


personaje.imprimir()