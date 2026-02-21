numeros = []
print("Ingrese números uno por uno.")
print("Escriba 0 para finalizar la entrada de datos.\n")
while True:
    numero = int(input("Ingrese un número: "))
    if numero == 0:
        break
    else:
        numeros.append(numero)
if len(numeros) > 0:
    mayor = numeros[0]
    for num in numeros:
        if num > mayor:
            mayor = num
    print("\nLos números ingresados fueron:", numeros)
    print("El número mayor es:", mayor)
else:
    print("\nNo se ingresaron números.")