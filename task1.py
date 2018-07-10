def is_leap_year():
    if 1900 <= year <= 10 ** 5 and year % 4 == 0 and \
            (year % 100 != 0 or year % 400 == 0):
        leap = True
        return leap
    else:
        leap = False
        return leap


year = int(input("Enter the year: "))
print(is_leap_year())
