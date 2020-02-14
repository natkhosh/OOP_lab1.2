# Лабораторная работа № 1.2

# Слушатель (ФИО): Мокрушина Н.Ю.


import datetime
from datetime import date

class Date:
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))

    def __init__(self, *args):
        """Examples:
            Format: year, month, day
            d1 = Date(2020, 2, 20)      # 20.2.2020
            d2 = Date()                 # current date
            d3 = Date(2020)             # current date
        """
        if len(args) >= 3:
            self.is_valid_date(args[0], args[1], args[2])
            self.__year = args[0]
            self.__month = args[1]
            self.__day = args[2]
        else:
            now = datetime.datetime.now()
            self.__year = now.year
            self.__month = now.month
            self.__day = now.day

    def __str__(self):
        return self.date

    def __repr__(self):
        return f'Date({self.__year!r}, {self.__month!r}, {self.__day!r})'

    def __int__(self):
        """  Override conversion type to int
        Example:
            date2 = Date(2020, 1, 12) --> 737985
        :return: days: int --> number of days
        """
        # года: текущий год делить на 3 = кол-во високосных их умножаем на 366, и прибавляем
        # текущий год минус високосные умноженные на 365
        print(f'Дата >  {self.__str__()}')
        days = ((self.__year // 3) * 366) + ((self.__year - (self.__year // 3)) * 365)
        # месяцы: идем в цикле от первого месяца до текущего и суммиурем дни в месяцах
        for i in range(1, self.__month):
            days += self.get_max_day(self.__year, i)
        # дни: суммируем текущий день
        days += self.__day
        return days

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
        if date2 < date1:
            raise ValueError
        else:
            days_diff = date2.__int__() - date1.__int__()
            print(f'Разница дней: {days_diff}')



if __name__ == "__main__":
    date_my = Date(2020, 4, 12)
    print(f'Число дней: {date_my.__int__()}')

    date1 = Date(2019, 1, 22)
    date2 = Date(2020, 1, 12)

    # dateSub = Date.date2_date1(date2, date1)
    # print(f'Число дней: {dateSub}')
    date_my.day = 5
    print(date_my.day)
    print(date_my.__str__())
#
# # print(date1.__int__())
# print(date2.__int__())



# print(date1.__int2__(date1))
# print(date2.__int2__(date2))


# d1 = Date(2020, 1, 10)
# print(d1.__sub__(6))
# d1_1 = Date(2020, 2, 7)
# d3 = Date()
# print(d3.__str__())
# print('----')

#
# 100 + d1_1
# # print('----')
# d1 - 5
# print(d1)

# print('---')
# d1 + 11