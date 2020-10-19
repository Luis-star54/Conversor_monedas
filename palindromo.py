menu = """

    Bienvenido al juego de pabaras 
"""
print(menu)

def palindromo(palabra):
    palabra = palabra.replace(" " , "").lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("Escribe un palindromo: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("es un palindromo")
    else:
        print("no es un palindromo")


if __name__ == "__main__":
    run()
