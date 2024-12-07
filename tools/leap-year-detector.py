def is_leap_year(year):
  if year < 0 or year != int(year):
    raise ValueError("Invalid year. Please enter a valid year.")
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

try:
  year = int(input("Enter a year: "))
  if is_leap_year(year):
    print(f"{year} is a leap year")
  else:
    print(f"{year} is not a leap year")
except ValueError:
  print("Invalid year.")