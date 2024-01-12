# Программирование на языке высокого уровня (Python).
# Задание №04_03_04.
#вариант 19
# Выполнил: Хасензода Муборакшох .Л.
# Группа: ПИН-б-о-22-1
# E-mail: muborremix@gmail.com

import json

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

    def __add__(self, other):
        # Реализация сложения дат
        pass

    def __sub__(self, other):
        # Реализация вычитания дат
        pass

    @classmethod
    def from_string(cls, str_value):

        pass

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump({'year': self.year, 'month': self.month, 'day': self.day}, file)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            return cls(data['year'], data['month'], data['day'])

    # Прочие методы и свойства
    def is_valid(self):
        # Проверка корректности даты
        pass

    @property
    def is_weekend(self):
        # Проверка, является ли день выходным
        pass

    def days_until(self, other_date):
        # Расчет количества дней до другой даты
        pass
