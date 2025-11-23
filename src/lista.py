# src/lista.py
# Importamos las funciones estaEnRango y estaEnLista desde el módulo1 funciones
from modulo1.funciones import estaEnRango, estaEnLista

if __name__ == "__main__":
    try:
        # Intentamos obtener un valor entero del usuario
        valor = int(input("Introduce un valor del 1 al 20: "))
    except ValueError:
        # Si el usuario no introduce un número válido, mostramos error y salimos
        print("Error: Debes introducir un número entero válido.")
    else:
        # Lista donde se comprobará si el valor está presente
        lista_numeros = [6, 14, 11, 3, 2, 1, 15, 19]

        # Comprobamos si el valor está dentro del rango 1 a 20
        if estaEnRango(valor, 1, 20):
            print("Está en rango")

            # Si está en rango, comprobamos si está dentro de la lista dada
            if estaEnLista(valor, lista_numeros):
                print("Y está en la lista")
            else:
                print("Pero no está en la lista")
        else:
            # Mensaje si el valor está fuera del rango
            print("Valor fuera de rango")
