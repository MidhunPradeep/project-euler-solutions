"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.

    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.

    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is
    divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec
2000)?

Answer:
"""
from collections import OrderedDict

WEEKS = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
        if year % 100 != 0:
            return True

    return False


def get_months(year):
    months = OrderedDict()
    months["jan"] = 31
    months["feb"] = 29 if is_leap_year(year) else 28
    months["mar"] = 31
    months["apr"] = 30
    months["may"] = 31
    months["jun"] = 30
    months["jul"] = 31
    months["aug"] = 31
    months["sep"] = 30
    months["oct"] = 31
    months["nov"] = 30
    months["dec"] = 31

    return months


def get_answer_for_year(year, first_weekday):
    months = get_months(year)
    current_weekday = first_weekday
    sun_months = 0

    for month in months:
        while current_weekday >= 7:
            current_weekday -= 7

        if current_weekday == WEEKS.index("sun"):
            sun_months += 1

        current_weekday += months[month]

    return sun_months


def main():
    start = 1901
    end = 2000

    answer = 0

    current_year = start
    first_weekday = WEEKS.index("tue")

    while current_year <= end:
        if first_weekday >= 7:
            first_weekday -= 7

        answer += get_answer_for_year(current_year, first_weekday)

        if is_leap_year(current_year):
            first_weekday += 1

        first_weekday += 1
        current_year += 1

    print(answer)


main()
