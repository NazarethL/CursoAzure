import unittest
from tareas import agregar, borrar, imprime_tareas

class Test_tareas(unittest.TestCase):

    def test_si_agrego_nueva_tarea_len_de_tareas_crece_en_uno(self):
        tareas = []
        resultado = agregar(tareas)
        self.assertGreater(len(resultado),0, f"El resultado es: {resultado} y el esperado es mayor de 0.")

if __name__ == '__main__':
    unittest.main()