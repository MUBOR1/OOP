# Программирование на языке высокого уровня (Python).
# Задание №04_03_04.
#вариант 19
# Выполнил: Хасензода Муборакшох .Л.
# Группа: ПИН-б-о-22-1
# E-mail: muborremix@gmail.com

from date import Date

if __name__ == "__main__":
    date1 = Date(2022, 10, 15)
    print(date1)

    date2 = Date.from_string("2023-05-20")
    print(date2)

    print(date1 + date2)

    date1.save("date1.json")
    date3 = Date.load("date1.json")
    print(date3)
