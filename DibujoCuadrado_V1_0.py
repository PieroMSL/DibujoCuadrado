def dibujar_cuadrado(lado, caracter="*"):
    """Dibuja un cuadrado de un tamaño dado con un carácter específico.

    Args:
        lado (int): La longitud de un lado del cuadrado.
        caracter (str, optional): El carácter a utilizar para dibujar el cuadrado. 
                                  Defaults to "*".
    """

    # Primera línea
    print(caracter * lado)

    # Lados laterales
    for _ in range(lado - 2):
        print(caracter, end="")
        print(" " * (lado - 2), end="")
        print(caracter)

    # Última línea
    print(caracter * lado)

# Obtener el tamaño del cuadrado y el carácter a utilizar
lado = int(input("Ingrese el tamaño del lado del cuadrado: "))
caracter = input("Ingrese el carácter a utilizar (por defecto *): ") or "*"

# Dibujar el cuadrado
dibujar_cuadrado(lado, caracter)