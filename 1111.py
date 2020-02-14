# print(2020/4)
# print(2020/3)
# leap = (2020 // 3) * 366
# not_leap = (2020 - 673) * 365
# print('високосных годов: ', leap)
# print('не високосных годов: ', not_leap)
# # print(leap + not_leap)
# # print(2020*365)
#
# a = (leap + not_leap)
# b = a + 31 + 29 + 31
# c = b + 12
# print(a)
# print(b)
# print(c)
#
# a = (2019, 11, 1)
# b = (2020, 2, 12)
# year_a = a[0]
# month_a = a[1]
# day_a = a[2]
# year_b = b[0]
# month_b = b[1]
# day_b = b[2]
# print(f'{year_a} {month_a} {day_a}')
#
# y_ = b[0] - a[0]
# m_ = b[1] - a[1]
# d_ = b[2] - a[2]
# print(f'{y_} {m_} {d_}')
#
#
# print(355//365)
# print(355//12)
# print(355//365)
from datetime import date
d0 = date(2019, 1, 22)
d1 = date(2020, 1, 12)
delta = d1 - d0
print(delta.days)