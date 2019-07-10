import math


# to check whether the year is leap year or not.
def is_leap_year(y):
    leap = False
    if 1900 <= y <= 1 * math.pow(10, 5):
        if y % 4 == 0 or y % 400 == 0:
            leap = True
        elif y % 100 == 0:
            leap = False
        else:
            leap = False
    return leap


# OR
def is_leap(year):
    leap = False

    # Write your logic here
    if 1990 <= year <= 1 * math.pow(10, 5):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    leap = True
                else:
                    leap = False
            else:
                leap = True
    return leap


if __name__ == "__main__":
    year = int(input())
    print(is_leap(year))

    # year = int(input())
    # print(is_leap_year(year))
