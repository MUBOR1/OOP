# Программирование на языке высокого уровня (Python).
# Задание №04_03_05.
#вариант 19
# Выполнил: Хасензода Муборакшох .Л.
# Группа: ПИН-б-о-22-1
# E-mail: muborremix@gmail.com

from date import Date
import json

class DateCollection:
    def __init__(self, data=None):
        if data is None:
            data = []
        self._data = data

    def __str__(self):
        return ', '.join(str(date) for date in self._data)

    def __getitem__(self, index):
        return self._data[index]

    def add(self, value):
        self._data.append(value)

    def remove(self, index):
        del self._data[index]

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump([date.__dict__ for date in self._data], file)

    def load(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self._data = [Date(**date_dict) for date_dict in data]
