# Write a program that converts a given number of days into years, weeks, and days

def convert_days(toatl_days):
    years = toatl_days // 365
    remaning_days = toatl_days % 365

    months = remaning_days // 30
    remaning_days = remaning_days % 30

    weeks = remaning_days //7
    days = remaning_days % 7

    print(f"{toatl_days} days is equal to: ")
    print(f" {years} years, {months} months, {weeks} weeks, {days} days")

num_days = int(input("Enter the days: "))
convert_days(num_days)
    