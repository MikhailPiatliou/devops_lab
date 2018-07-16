def main():
    year = int(input("Enter the year: "))
    print(is_leap_year(year))


def is_leap_year(year):
    return (1900 <= year <= 10 ** 5 and year % 4 == 0 and
            (year % 100 != 0 or year % 400 == 0))


if __name__ == "__main__":
    main()
