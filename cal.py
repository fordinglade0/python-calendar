import calendar

def print_calendar(year, month):
    cal = calendar.month(year, month)
    print(cal)

def main():
    year = int(input("Введите год: "))
    month = int(input("Введите месяц: "))
    print_calendar(year, month)

if __name__ == "__main__":
    main()
