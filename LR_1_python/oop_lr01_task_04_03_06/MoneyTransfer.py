# Программирование на языке высокого уровня (Python).
# Задание №04_03_06.
#вариант 19
# Выполнил: Хасензода Муборакшох .Л.
# Группа: ПИН-б-о-22-1
# E-mail: muborremix@gmail.com

class MoneyTransfer:

    def __init__(self, sender, recipient, amount, execution_date, sender_bank_details, recipient_bank_details, commission, currency_characteristics):
        super().__init__(sender, recipient, amount, execution_date)
        self.sender_bank_details = sender_bank_details
        self.recipient_bank_details = recipient_bank_details
        self.commission = commission
        self.currency_characteristics = currency_characteristics

    def additional_info(self):
        # Логика получения дополнительной информации о переводе
        print(f"Additional information: Commission - {self.commission}, Currency Characteristics - {self.currency_characteristics}")
