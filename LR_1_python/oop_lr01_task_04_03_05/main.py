# Программирование на языке высокого уровня (Python).
# Задание №04_03_05.
#вариант 19
# Выполнил: Хасензода Муборакшох .Л.
# Группа: ПИН-б-о-22-1
# E-mail: muborremix@gmail.com

from date import Date
from date_collection import DateCollection

if __name__ == "__main__":
    date1 = Date(2022, 10, 15)
    date2 = Date.from_string("2023-05-20")

    collection = DateCollection([date1, date2])

    print("Initial Collection:")
    print(collection)

    date3 = Date(2023, 12, 31)
    collection.add(date3)

    print("\nCollection after adding date3:")
    print(collection)

    collection.remove(0)  # Remove the first date in the collection

    print("\nCollection after removing the first date:")
    print(collection)

    collection.save("dates.json")

    new_collection = DateCollection()
    new_collection.load("dates.json")

    print("\nNew Collection loaded from file:")
    print(new_collection)
