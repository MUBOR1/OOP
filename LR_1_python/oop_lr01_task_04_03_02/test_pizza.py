# Программирование на языке высокого уровня (Python).
# Задание №04_03_02. Вариант 02
#
# Выполнил: Хасензода Муборакшох .Л.
# Группа: ПИН-б-о-22-1
# E-mail: muborremix@gmail.com

import unittest
from io import StringIO
from unittest.mock import patch
from терминал import Терминал

class TestТерминал(unittest.TestCase):

    @patch("builtins.input", side_effect=["1", "0", "500", "2", "-1", "3", "0", "600", "-"])
    def test_терминал(self, mock_input):
        терминал = Терминал()

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            терминал.показать_меню()
            expected_output1 = "...\n<Ожидаемый вывод консоли при отображении меню>\n..."
            self.assertIn(expected_output1, mock_stdout.getvalue())

            терминал.обработать_команду("1")
            терминал.обработать_команду("0")

            # Проверьте, что вывод равен ожидаемому значению для терминала и команды "0"

            терминал.обработать_команду("500")

            # Добавьте проверку для вывода в случае недостаточной суммы для заказа

            терминал.обработать_команду("2")
            терминал.обработать_команду("-1")

            # Проверьте, что вывод равен ожидаемому значению для терминала и отрицательной команды

            терминал.обработать_команду("3")
            терминал.обработать_команду("0")
            терминал.обработать_команду("600")
            expected_output2 = "...\n<Ожидаемый вывод консоли при определенной последовательности команд>\n..."
            self.assertIn(expected_output2, mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()
