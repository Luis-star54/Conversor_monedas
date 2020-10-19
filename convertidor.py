menu = """
    Bienvenido al mejor conversor de monedas 

1 - elige pesos colombianos
2 - eliges pesos argentinos
3 - eliges pesos mexicanos
elige la tasa de cambio de tu preferencia
 """
tasa_cambio = int(input(menu))
dinero = float(input("cuanto dinero quieres cambiar?: "))
def monedas(precios):
    cambio = precios
    cambio_de_pesos = dinero / cambio
    cambio_de_pesos = round(cambio_de_pesos , 2)
    cambio_de_pesos = str(cambio_de_pesos)
    print("tienes $ " + cambio_de_pesos + " dolares")
if tasa_cambio == 1:
    monedas(3847)
elif tasa_cambio == 2:
    monedas(70)
elif tasa_cambio == 3:
    monedas(21)
else:
    print("ingresa los datos correctos por favor ")