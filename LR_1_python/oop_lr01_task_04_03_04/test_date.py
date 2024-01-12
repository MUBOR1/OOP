# Программирование на языке высокого уровня (Python).
# Задание №04_03_04.
#вариант 19
# Выполнил: Хасензода Муборакшох .Л.
# Группа: ПИН-б-о-22-1
# E-mail: muborremix@gmail.com

import unittest
from date import Date

class TestDateMethods(unittest.TestCase):
    def test_constructor(self):
        date = Date(2022, 10, 15)
        self.assertEqual(str(date), "15/10/2022")

    def test_from_string(self):
        date = Date.from_string("2023-05-20")
        self.assertEqual(str(date), "20/05/2023")

    # Другие методы тестирования

if __name__ == '__main__':
    unittest.main()
