# Программирование на языке высокого уровня (Python).
# Задание №04_03_01. Вариант 01
#
# Выполнил: Хасензода Муборакшох .Л.
# Группа: ПИН-б-о-22-1
# E-mail: muborremix@gmail.com

import unittest
from roman import Roman

class TestRomanClass(unittest.TestCase):
    def test_init_valid_integer_input(self):
        roman_number = Roman(2021)
        self.assertEqual(roman_number._arabic, 2021)

    def test_init_valid_roman_input(self):
        roman_number = Roman("MMXXI")
        self.assertEqual(roman_number._arabic, 2021)

    def test_init_invalid_input(self):
        with self.assertRaises(TypeError):
            Roman(3.14)

    def test_add_roman(self):
        roman_number1 = Roman(1000)
        roman_number2 = Roman(999)
        result = roman_number1 + roman_number2
        self.assertEqual(str(result), "MCMXCIX")

    def test_add_integer(self):
        roman_number = Roman(2021)
        result = roman_number + 1
        self.assertEqual(str(result), "MMXXII")

    def test_sub_roman(self):
        roman_number1 = Roman(2021)
        roman_number2 = Roman(1000)
        result = roman_number1 - roman_number2
        self.assertEqual(str(result), "MXXI")

    # Другие тесты на операции умножения, целочисленного деления и истинного деления можно также написать

    def test_to_roman(self):
        roman = Roman.to_roman(2021)
        self.assertEqual(roman, "MMXXI")

    def test_to_arabic(self):
        arabic = Roman.to_arabic("MMXXI")
        self.assertEqual(arabic, 2021)

if __name__ == '__main__':
    unittest.main()
