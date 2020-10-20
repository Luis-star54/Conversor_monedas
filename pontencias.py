
def run():
    numero = int(input("elige un  numero entero "))
    LIMITE = 1000
    contenedor = 0
    resultado = numero**contenedor
    while resultado < LIMITE:
        print(str(numero) + "elvado a " + str(contenedor) + "es igual a " + str(resultado))
        contenedor = contenedor + 1
        resultado = numero**contenedor

if __name__ == "__main__":
    run()