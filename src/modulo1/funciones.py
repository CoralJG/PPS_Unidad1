# src/modulo1/funciones.py
def esBinario(strbinario):
    """
    Comprueba si la cadena strbinario contiene únicamente caracteres '0' o '1'.
    Devuelve True si todos los caracteres son binarios, False en caso contrario.
    """
    return all(c in '01' for c in strbinario)


def estaEnRango(valor, minimo, maximo):
    """
    Determina si el valor está dentro del rango [minimo, maximo].
    Devuelve True si minimo <= valor <= maximo, en caso contrario False.
    """
    return minimo <= valor <= maximo


def estaEnLista(valor, lista):
    """
    Comprueba si el valor está contenido en la lista recibida.
    Devuelve True si valor está en lista, False en caso contrario.
    """
    return valor in lista
