'''Компьютерный формат даты и времени обычно выглядит так: 21.05.2018 16:30
Люди предпочитают видеть эту же информацию в более развернутом виде: 21 May 2018 year, 16 hours 30 minutes
Ваша задача - преобразовать дату и время из числового формата и словесно-числовой.
Входные данные: Дата и время как строка, состоящая из чисел (например: 14.02.2018 16:55)

Выходные данные: Та же самая дата и время, но в более развернутом формате'''
from datetime import datetime
import calendar

def date_time(time: str) -> str:
    #replace this for solution
    dt = datetime.strptime(time, '%d.%m.%Y %H:%M')
    time = f"{dt.day} {calendar.month_name[dt.month]} {dt.year} year {dt.hour} hours {dt.minute} minutes"
    if dt.hour == 1:
        time = time.replace('hours', 'hour')
    if dt.minute == 1:
        time = time.replace('minutes', 'minute')
    return time

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 01:01'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")

