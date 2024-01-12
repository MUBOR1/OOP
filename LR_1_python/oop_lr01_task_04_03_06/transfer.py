# Программирование на языке высокого уровня (Python).
# Задание №04_03_06.
#вариант 19
# Выполнил: Хасензода Муборакшох .Л.
# Группа: ПИН-б-о-22-1
# E-mail: muborremix@gmail.com

class Transfer:
    def __init__(self, sender, recipient, amount, execution_date):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.execution_date = execution_date

    def execute(self):
        # Логика выполнения перевода
        print(f"Transfer of {self.amount} from {self.sender} to {self.recipient} executed on {self.execution_date}")
