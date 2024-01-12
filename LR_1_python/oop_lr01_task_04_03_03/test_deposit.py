# Программирование на языке высокого уровня (Python).
# Задание №04_03_03. Вариант 03
#
# Выполнил: Хасензода Муборакшох .Л.
# Группа: ПИН-б-о-22-1
# E-mail: muborremix@gmail.com

import unittest
from deposit import deposits

class TestMain(unittest.TestCase):

    def test_main(self):
        with patch('builtins.input', side_effect=['1', '1000', '12', '']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                main()
                expected_output = "..."
                self.assertEqual(mock_stdout.getvalue(), expected_output)

class TestDeposit(unittest.TestCase):

    def test_get_profit(self):
        deposit = deposits[0]
        profit = deposit.get_profit(1000, 12)
        self.assertEqual(profit, 50)

if __name__ == '__main__':
    unittest.main()
