contador = 0
acumulador = 0

while True:
    numero = int(input("introduce un numero (0 para terminar):"))

    if numero == 0:
        break

    acumulador += numero
    contador += 1


media = acumulador / contador
# imprimimos la sumay la media 
print(f"la suma de los numeros introducidos es: {acumulador}")
print(f"la media de los numeros introducidos es:{media}")
print("no se han introducido numeros validos.")
