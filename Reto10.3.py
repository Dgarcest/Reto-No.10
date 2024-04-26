#Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.

def crear_arreglos(): #funcion para crear la lista
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
    arreglo = crear_arreglos()
    for i in arreglo: #recorre todos los valores de la lista
        if i == 0: #si el valor es 0 lo remueve y lo pone al final
            arreglo.remove(0)
            arreglo.append(0)
    print(f"la lista con todos los ceros que aparecen en el arreglo al final es {arreglo}")