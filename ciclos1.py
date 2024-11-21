numero = int(input("introduce un numero para calculart su factorial: "))

factorial = 1

if  numero <0:
    print("el factorial no esta definido para numeros negativos.")
else:
    for i in range(1, numero + 1):
        factorial *=i
        print(f"El factorial de {numero} es factorial {factorial}")
    