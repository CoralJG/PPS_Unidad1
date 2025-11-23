# src/tests/test_modulo1.py
import unittest
from modulo1.funciones import esBinario, estaEnRango, estaEnLista

class TestFunciones(unittest.TestCase):
    # Test para la función esBinario
    def test_esBinario(self):
        self.assertTrue(esBinario("1001"))  
        self.assertFalse(esBinario("Hola")) 
        self.assertFalse(esBinario("102")) 

    # Test para la función estaEnRango
    def test_estaEnRango(self):
        self.assertTrue(estaEnRango(10, 1, 20)) 
        self.assertFalse(estaEnRango(0, 1, 20))  
        self.assertFalse(estaEnRango(21, 1, 20))

    # Test para la función estaEnLista
    def test_estaEnLista(self):
        lista = [6, 14, 11, 3, 2, 1, 15, 19]
        self.assertTrue(estaEnLista(6, lista))  
        self.assertFalse(estaEnLista(7, lista))
    
    # Test que verifica que esBinario lance excepción para entrada no binaria
    def test_esBinario_excepcion(self):
        with self.assertRaises(TypeError):
            # Forzamos un error pasando algo que no sea string
            esBinario(None)

if __name__ == "__main__":
    # Ejecuta todos los tests definidos cuando se ejecuta el script directamente
    unittest.main()
