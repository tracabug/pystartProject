from datetime import date, datetime

# Get current date
today = date.today()
today_form = today.strftime('%d/%m/%Y')
# Get date of birth (dob)
dob_day = int(input('Please enter your birth day: '))
dob_month = int(input('Please enter your birth month: '))
dob_year = int(input('Please enter your birth year: '))

# Convert user input into datetime object
DoB = date(dob_year, dob_month, dob_day).strftime('%d/%m/%Y')


# Calculate the years difference
year_diff = today.year - dob_year
# Check if birth month and birthday precede current month and current day
month_day_diff = ((today.month, today.day) <= (dob_month, dob_day))
# Calculate the user's age
age = year_diff - month_day_diff

if DoB == today_form:
    print(f'Hello little baby.')
if today.day == dob_day and today.month == dob_month:
    print(f"Happy birthday! You are now {age.years} years old.")
else:
    print(f'You are {age} years old')

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (dob_year % 400 == 0) and (dob_year % 100 == 0):
    print("{0} is a leap year".format(dob_year))
# not divided by 100 means not a century year
#  divided by 4 is a leap year
elif (dob_year % 4 ==0) and (dob_year % 100 != 0):
    print("{0} is a leap year".format(dob_year))
# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(dob_year))
