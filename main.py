from DibujoCuadrado_V1_1 import Cuadrado

if __name__ == '__main__':
    # Obtener los datos del usuario
    lado = int(input("Ingrese el tamaño del lado del cuadrado: "))
    caracter = input("Ingrese el carácter a utilizar (por defecto *): ") or "*"

    # Crear un objeto Cuadrado y dibujarlo
    cuadrado = Cuadrado(lado, caracter)
    cuadrado.dibujar()