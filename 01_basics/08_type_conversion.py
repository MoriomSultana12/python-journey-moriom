# Taking user's birth year as input (input always returns a string)
birth_year = input('Enter birth year:')

# Converting the birth year from string to integer using int()
# Then calculating age by subtracting birth year from current year (2026)
age = 2026-int(birth_year)

# Printing the calculated age
print(age)
