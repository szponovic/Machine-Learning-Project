import unittest
import functions

class TestFunctions(unittest.TestCase):
    def test_create_table(self):
        file_path = "Screen-Time-Data.csv"
        self.assertIsNone(functions.create_table(file_path))

    def test_box_plot(self):
        self.assertIsNone(functions.box_plot())

    def test_display_statistics(self):
        self.assertIsNone(functions.display_statistics())



# python -m unittest tests.py


# class TestFunctions(unittest.TestCase):
#     def test_create_table(self):
#         file_path = "Screen-Time-Data.csv"
#         expected_output = "|   |   |   |   |   |   |   |   |   |\n+---+---+---+---+---+---+---+---+---+\n"
#         self.assertEqual(functions.create_table(file_path), expected_output)
#
#     def test_box_plot(self):
#         self.assertIsNone(functions.box_plot())
#
#     def test_display(self):
#         expected_output = "Wybierz opcje: \n1 - tabela \n2 - info \n3 - wykres pudelkowy\n4 - histogram\n5 - Wartosc max\n6 - Korelacja\n7 - Testowanie modeli\n0 - Zakoncz\n"
#         self.assertEqual(functions.display(), expected_output)
#
#     def test_choices(self):
#         self.assertEqual(functions.choices("1"), "--tabela--")
#         self.assertEqual(functions.choices("8"), "Zly wybor")