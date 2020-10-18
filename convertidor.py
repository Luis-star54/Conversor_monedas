menu = """
    Bienvenido al mejor conversor de monedas 

1 - elige pesos colombianos
2 - eliges pesos argentinos
3 - eliges pesos mexicanos
elige la tasa de cambio de tu preferencia
 """
tasa_cambio = int(input(menu))
dinero = float(input("cuanto dinero quieres cambiar?: "))
if tasa_cambio == 1:
    cambio = 3847
    cambio_de_pesos = dinero / cambio
    cambio_de_pesos = round(cambio_de_pesos , 2)
    cambio_de_pesos = str(cambio_de_pesos)
    print("tienes $ " + cambio_de_pesos + " dolares")
elif tasa_cambio == 2:
    cambio = 77.5
    cambio_dolar =  dinero / cambio
    cambio_dolar = round(cambio_dolar , 2)
    cambio_dolar = str(cambio_dolar)
    print("tienes $ " + cambio_dolar + " dolares")
elif tasa_cambio == 3:
    cambio = 21
    cambio_dolar =  dinero / cambio
    cambio_dolar = round(cambio_dolar , 2)
    cambio_dolar = str(cambio_dolar)
    print("tienes $ " + cambio_dolar + " dolares")
else:
    print("ingresa los datos correctos por favor ")