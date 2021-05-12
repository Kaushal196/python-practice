monts_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0) 

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return "Invalid month"
    if month == 2 and is_leap_year(year):
        return 29
    return monts_days[month]

print(days_in_month(2016, 2))
#op-> 29

print(days_in_month(2021, 2))
#op-> 28

print(days_in_month(2021, 4))
#op-> 30

print(days_in_month(2021, 14))
#op-> Invalid month