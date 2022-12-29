# Leap Year 
print("CHECK DAYS IN A MONTH")
year = int(input("Enter the year you want to check:\n>> "))
month = int(input("Enter the month:\n>> "))

def check_leap_year(year_input):
    if year_input % 4 == 0:
        if year_input % 100 == 0:
            if year_input % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(usr_year, usr_month):
    if usr_month < 1 or usr_month > 12:
        return "Invalid Input"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 30, 31, 30]
    is_leap = check_leap_year(year_input=usr_year)
    if is_leap == True:
        if usr_month == 2:
            return 29
    else:
        return month_days[usr_month - 1]

print(days_in_month(usr_year=year, usr_month=month))