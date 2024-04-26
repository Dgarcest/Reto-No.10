#Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

def crear_arreglos(): #funcion para crear las 2 listas
    arreglo = [] #lista vacia que se irá llenando
    while True:
        numero = input("Escriba el numero que quiere ingresar (o 'terminar' para acabar): ")

        if numero.lower() == "terminar": #unicamente con la palabra "terminar" termina el codigo
            break
        try: #intentara pasar el numero a flotante y ponerlo en la lista, si no puede ejecutara el except 
            numero = float(numero)
            arreglo.append(numero)
        except: #este except se ejecutara probablemente porque se puso un str en la variable numero (uno diferente a "terminar")
            print('Ingrese un numero entero o flotante o la palabra "terminar" para acabar')
    return arreglo #devuelve la lista que ya está llena

if __name__ == "__main__":
    #se utiliza la funcion para crear los 2 arreglos y ponerlos en las variables "arreglo1" y "arreglo2"
    print("A continuacion escriba los valores del primer arreglo:")
    arreglo1 = crear_arreglos()
    print("A continuacion escriba los valores del segundo arreglo:")
    arreglo2 = crear_arreglos()

    if len(arreglo1) == len(arreglo2): #si los arreglos tienen la misma longitud
        suma = 0
        for i in range(len(arreglo1)): #ciclo que es la suma de los respectivos productos
            producto = arreglo1[i] * arreglo2[i]
            suma += producto 
        print(f"El producto escalar de los 2 vectores o arreglos es de {suma}")

    else:
        print("los arreglos tienen distintos tamaños")