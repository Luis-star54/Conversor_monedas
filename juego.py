import random #la forma en que importamos datos nativos de los desarrolladores de python, en este caso aleatorios 

def run(): #funcion, ayuda a no escribir lineas de codigos similares, dentro de ellas podemos declarar  parametos 
    numero_aleatorio = random.randint(1 , 100)
    numero_usuario = int(input("Escribe un numero del 1 al 100: "))
    while numero_usuario != numero_aleatorio: # esto es un ciclo , agiliza tareas repetitivas 
        if numero_usuario < numero_aleatorio:
            print("escribe un numero mayor ")
        else:
            print("escribe un numero menor ")
        numero_usuario = int(input("escribe otro numero: "))
    print("Ganaste, eres un excelente adivinador")            



if __name__ == "__main__": #se le conoce como un enterpoint es la forma estandar de comer los programas en python, y tambien se invoca la funcion de arranque 
    run()
