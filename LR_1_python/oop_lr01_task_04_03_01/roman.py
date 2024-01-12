# Программирование на языке высокого уровня (Python).
# Задание №04_03_01. Вариант 01
#
# Выполнил: Хасензода Муборакшох .Л.
# Группа: ПИН-б-о-22-1
# E-mail: muborremix@gmail.com


class Roman:
    ARABIC_MIN = 1
    ARABIC_MAX = 3999
    ROMAN_MIN = "I"
    ROMAN_MAX = "MMMCMXCIX"

    LETTERS = ["M", "CM", "D", "CD", "C", "XC", "L",
               "XL", "X", "IX", "V", "IV", "I"]
    NUMBERS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    def __init__(self, value):
        if not isinstance(value, (int, str)):
            raise TypeError("Cannot create Roman number from {0}".format(type(value)))

        if isinstance(value, int):
            self.__check_arabic(value)
            self._arabic = value
        elif isinstance(value, str):
            self.__check_roman(value)
            self._arabic = self.to_arabic(value)

    def __add__(self, other):
        if isinstance(other, Roman):
            result = self._arabic + other._arabic
        elif isinstance(other, int):
            result = self._arabic + other
        else:
            raise TypeError("Unsupported operand type for +: '{0}' and '{1}'".format(
                type(self).__name__, type(other).__name__))

        return Roman(result)

    def __sub__(self, other):
        if isinstance(other, Roman):
            result = self._arabic - other._arabic
        elif isinstance(other, int):
            result = self._arabic - other
        else:
            raise TypeError("Unsupported operand type for -: '{0}' and '{1}'".format(
                type(self).__name__, type(other).__name__))

        return Roman(result)

    def __mul__(self, other):
        if isinstance(other, Roman):
            result = self._arabic * other._arabic
        elif isinstance(other, int):
            result = self._arabic * other
        else:
            raise TypeError("Unsupported operand type for *: '{0}' and '{1}'".format(
                type(self).__name__, type(other).__name__))

        return Roman(result)

    def __floordiv__(self, other):
        if isinstance(other, Roman):
            result = self._arabic // other._arabic
        elif isinstance(other, int):
            result = self._arabic // other
        else:
            raise TypeError("Unsupported operand type for //: '{0}' and '{1}'".format(
                type(self).__name__, type(other).__name__))

        return Roman(result)

    def __truediv__(self, other):
        return self.__floordiv__(other)

    def __str__(self):
        return Roman.to_roman(self._arabic)

    @staticmethod
    def __check_arabic(value):
        if not (Roman.ARABIC_MIN <= value <= Roman.ARABIC_MAX):
            raise ValueError("Arabic number {0} is out of range [{1}-{2}]".format(
                value, Roman.ARABIC_MIN, Roman.ARABIC_MAX))

    @staticmethod
    def __check_roman(value):
        for letter in value:
            if letter not in Roman.LETTERS:
                raise ValueError("Invalid Roman number: {0}".format(value))

    @staticmethod
    def to_arabic(roman):
        def letter_to_number(letter):
            return Roman.NUMBERS[Roman.LETTERS.index(letter.upper())]

        Roman.__check_roman(roman)

        i = 0
        value = 0

        while i < len(roman):
            number = letter_to_number(roman[i])
            i += 1

            if i == len(roman):
                value += number
            else:
                next_number = letter_to_number(roman[i])
                if next_number > number:
                    value += next_number - number
                    i += 1
                else:
                    value += number

        Roman.__check_arabic(value)
        return value

    @staticmethod
    def to_roman(arabic):
        Roman.__check_arabic(arabic)

        roman = ""
        n = arabic

        for i, number in enumerate(Roman.NUMBERS):
            while n >= number:
                roman += Roman.LETTERS[i]
                n -= Roman.NUMBERS[i]

        return roman