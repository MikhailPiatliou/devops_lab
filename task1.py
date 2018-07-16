def is_leap_year():
    return (1900 <= year <= 10 ** 5 and year % 4 == 0 and
            (year % 100 != 0 or year % 400 == 0))


year = int(input("Enter the year: "))
print(is_leap_year())
