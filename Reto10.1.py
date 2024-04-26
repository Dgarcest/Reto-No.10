#Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

#se declaran las 2 variables, la lista y la variable suma para el ciclo for
arreglo = []
suma = 0

while True: 
    numero = input("Escriba el numero que quiere ingresar (o 'terminar' para acabar): ")

    if numero.lower() == "terminar": #unicamente con la palabra "terminar" termina el codigo
        break
    try: #intentara pasar el numero a flotante y ponerlo en la lista, si no puede ejecutara el except 
        numero = float(numero)
        arreglo.append(numero)
    except: #este except se ejecutara probablemente porque se puso un str en la variable numero (uno diferente a "terminar")
        print('Ingrese un numero entero o flotante o la palabra "terminar" para acabar')

for i in arreglo: #ciclo que suma todas las valores de la lista
    suma += i

promedio = suma/len(arreglo) #el promedio

print(f"el promedio de el arreglo de reales {arreglo} es: {promedio}")