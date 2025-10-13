from datetime import date
day = int(input("Enter your birth day (1-31):"))
month = int(input("Enter your birth month (1-12):"))
year = int(input("Enter your birth year (YYYY):"))

today = date.today()
age = today.year - year
if (today.month,today.day) < (month, day):
    age -= 1
print("Your age is:",age)