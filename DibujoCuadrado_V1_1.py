class Figura:
    def dibujar(self):
        pass  # Méttodo abstracto, será implementado por las subclases

class Cuadrado(Figura):
    def __init__(self, lado, caracter="*"):
        self.lado = lado
        self.caracter = caracter

    def dibujar(self):
        """Dibuja el cuadrado."""
        # Primera línea
        print(self.caracter * self.lado)

        # Lados laterales
        for _ in range(self.lado - 2):
            print(self.caracter, end="")
            print(" " * (self.lado - 2), end="")
            print(self.caracter)

        # Última línea
        print(self.caracter * self.lado)