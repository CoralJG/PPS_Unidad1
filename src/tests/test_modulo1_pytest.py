# tests/test_modulo1_pytest.py
import pytest
from modulo1.funciones import esBinario, estaEnRango, estaEnLista

def test_esBinario():
    # Verifica que cadenas binarias válidas retornen True
    assert esBinario("1001") is True
    # Verifica que cadenas con caracteres no binarios retornen False
    assert esBinario("Hola") is False
    assert esBinario("102") is False

def test_estaEnRango():
    # Verifica que valores dentro del rango retornen True
    assert estaEnRango(10, 1, 20) is True
    # Verifica valores fuera del rango retornen False
    assert estaEnRango(0, 1, 20) is False
    assert estaEnRango(21, 1, 20) is False

def test_estaEnLista():
    lista = [6, 14, 11, 3, 2, 1, 15, 19]
    # Verifica que valores en lista retornen True
    assert estaEnLista(6, lista) is True
    # Verifica que valores no en lista retornen False
    assert estaEnLista(7, lista) is False

def test_esBinario_excepcion():
    # Test para validar que se lance un TypeError 
    # si esBinario recibe None (o similar)
    with pytest.raises(TypeError):
        esBinario(None)
