#TODO
# + 1. Реализовать класс Date согласно шаблону
#     1.1 Конструктор класса
#     1.2 Свойства для дня, месяца, года
#     1.3 Сеттеры и геттеры для свойств
# + 2. Реализовать методы add_day, add_month, add_year
# 3. Переопределить магические методы для класса Date:
#    + __lt__(self, other) - x < y вызывает x.__lt__(y).
#    + __le__(self, other) - x ≤ y вызывает x.__le__(y).
#    + __eq__(self, other) - x == y вызывает x.__eq__(y).
#    + __ne__(self, other) - x != y вызывает x.__ne__(y)
#    + __gt__(self, other) - x > y вызывает x.__gt__(y).
#    + __ge__(self, other) - x ≥ y вызывает x.__ge__(y).
# 4. Перегрузка арифметических операторов для класса Date:
#     __add__(self, other) - сложение. x + y вызывает x.__add__(y).
#     __sub__(self, other) - вычитание (x - y).
#     __radd__(self, other).
#     __rsub__(self, other).
#     __iadd__(self, other) - +=.
#     __isub__(self, other) - -=.
# + 5. Переопределить преобразование типа в int.
#     __int__(self)
# + 6. Перегрузить конструктор класса
# 7. Написать тесты для проверки реализованного функционала (Необязательное)

import datetime


class Date:
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))

    def __init__(self, *args):
        if len(args) == 0:
            now = datetime.datetime.now()
            self.__year = now.year
            self.__month = now.month
            self.__day = now.day
        else:
            self.is_valid_date(args[0], args[1], args[2])
            self.__year = args[0]
            self.__month = args[1]
            self.__day = args[2]

    def __str__(self):
        return self.date

    def __repr__(self):
        return f'Date({self.__year!r}, {self.__month!r}, {self.__day!r})'

    def __lt__(self, other):
        if self.__year < other.year:
            return True
        elif self.__year > other.year:
            return False
        else:
            if self.__month < other.month:
                return True
            elif self.__month > other.month:
                return False
            else:
                if self.__day < other.day:
                    return True
                elif self.__day >= other.day:
                    return False

    def __le__(self, other):
        if self.__year <= other.year:
            return True
        elif self.__year > other.year:
            return False
        else:
            if self.__month <= other.month:
                return True
            elif self.__month > other.month:
                return False
            else:
                if self.__day <= other.day:
                    return True
                elif self.__day > other.day:
                    return False

    def __eq__(self, other):
        if (self.__day == other.day) and (self.__month == other.month) and (self.__year == other.year):
            return True
        else:
            return False

    def __ne__(self, other):
        if (self.__day != other.day) or (self.__month != other.month) or (self.__year != other.year):
            return True
        else:
            return False

    def __gt__(self, other):
        if self.__year > other.year:
            return True
        elif self.__year < other.year:
            return False
        else:
            if self.__month > other.month:
                return True
            elif self.__month < other.month:
                return False
            else:
                if self.__day > other.day:
                    return True
                elif self.__day <= other.day:
                    return False

    def __ge__(self, other):
        if self.__year >= other.year:
            return True
        elif self.__year < other.year:
            return False
        else:
            if self.__month >= other.month:
                return True
            elif self.__month < other.month:
                return False
            else:
                if self.__day >= other.day:
                    return True
                elif self.__day < other.day:
                    return False

    def __int__(self):
        return self.__year * 365 + self.__month * 30 + self.__day

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    @property
    def date(self):
        return f'{self.__day}.{self.__month}.{self.__year}'

    @staticmethod
    def is_leap_year(year):
        if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
            return True
        else:
            return False

    @classmethod
    def get_max_day(cls, year, month):
        leap_year = 1 if cls.is_leap_year(year) else 0
        return cls.DAY_OF_MONTH[leap_year][month - 1]

    @classmethod
    def is_valid_date(cls, year, month, day):
        if not isinstance(year, int):
            raise TypeError('year must be int')
        if not isinstance(month, int):
            raise TypeError('month must be int')
        if not isinstance(day, int):
            raise TypeError('day must be int')

        if not 0 < month <= 12:
            raise ValueError('month must be 0 < month <= 12')

        if not 0 < day <= cls.get_max_day(year, month):
            raise ValueError('invalid day for this month and year')

    @day.setter
    def day(self, value):
        value = int(value)
        self.is_valid_date(self.__year, self.__month, value)
        self.__day = value

    @month.setter
    def month(self, value):
        value = int(value)
        self.is_valid_date(self.__year, value, self.__day)
        self.__month = value

    @year.setter
    def year(self, value):
        value = int(value)
        self.is_valid_date(value, self.__month, self.__day)
        self.__year = value

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError('Date must be str')
        value = value.split('.')
        if len(value) != 3:
            raise ValueError('Invalid date format')

        try:
            day = int(value[0])
            month = int(value[1])
            year = int(value[2])
            self.is_valid_date(year, month, day)
        except:
            raise ValueError('Invalid date format')

        self.__day = day
        self.__month = month
        self.__year = year

    def add_year(self, year):
        self.__year += year
        return self.__year

    def add_month(self, month):
        months = self.__month + month
        if months > 12:
            self.__month = months % 12
            self.add_year(int(months // 12))
            return self.__month
        else:
            self.__month += month
            return self.__month

    def add_day(self, day):
        days = self.__day + day
        if days > self.get_max_day(self.__year, self.__month):
            days -= self.get_max_day(self.__year, self.__month)
            self.add_month(1)
            self.__day = 0
            self.add_day(days)
        else:
            self.__day = days
            return self.__day

    @staticmethod
    def date2_date1(date2, date1):
        pass


date_my = Date(2020, 10, 11)
date_now = Date(10)
print(date_my)
print(date_now)

