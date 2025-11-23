# src/binario.py
# Importamos la función esBinario desde el módulo1 funciones
from modulo1.funciones import esBinario

def binario_a_decimal(strbinario):
    """
    Convierte una cadena binaria válida a decimal.
    Primero verifica si la cadena es binaria usando la función esBinario.
    Si no es binaria, lanza un ValueError.
    Si es válida, convierte la cadena a un número decimal.
    """
    if not esBinario(strbinario):
        raise ValueError("No es número binario válido")
    return int(strbinario, 2)

if __name__ == "__main__":
    # Pedimos al usuario que introduzca un número binario como cadena
    binario = input("Introduce un número binario: ")
    
    try:
        # Intentamos convertir el número binario a decimal
        decimal = binario_a_decimal(binario)
    except ValueError as e:
        # Si la cadena no es válida, mostramos un mensaje de error
        print("Error:", e)
    else:
        # Si no hubo error, mostramos el número decimal resultante
        print("Número decimal:", decimal)



