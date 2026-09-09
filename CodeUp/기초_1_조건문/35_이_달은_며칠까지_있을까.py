year, month = input().split()
month_last = [31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year) :
    return 1 if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) else 0

print(month_last[int(month) - 1] if month != "2" else month_last[int(month) - 1][is_leap(int(year))])
