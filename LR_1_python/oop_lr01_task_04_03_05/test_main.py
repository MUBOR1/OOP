# Программирование на языке высокого уровня (Python).
# Задание №04_03_05.
#вариант 19
# Выполнил: Хасензода Муборакшох .Л.
# Группа: ПИН-б-о-22-1
# E-mail: muborremix@gmail.com

import unittest
from main import Date, DateCollection

class TestDateCollection(unittest.TestCase):
    def test_date_collection_operations(self):
        date1 = Date(2022, 10, 15)
        date2 = Date.from_string("2023-05-20")
        date3 = Date(2023, 12, 31)

        collection = DateCollection([date1, date2])

        self.assertEqual(str(collection), "2022-10-15, 2023-05-20")

        collection.add(date3)

        self.assertEqual(str(collection), "2022-10-15, 2023-05-20, 2023-12-31")

        collection.remove(0)

        self.assertEqual(str(collection), "2023-05-20, 2023-12-31")

        collection.save("test_dates.json")

        new_collection = DateCollection()
        new_collection.load("test_dates.json")

        self.assertEqual(str(new_collection), "2023-05-20, 2023-12-31")

if __name__ == '__main__':
    unittest.main()
