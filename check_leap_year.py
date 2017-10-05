# Python program to check if the input year is a leap year or not

# To get year (integer input) from the user
year = int(input("Enter a year: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print "{} year is leap year".format(year)
        else:
            print "{} year is not leap year".format(year)
    else:
        print "{} year is leap year".format(year)
else:
    print "{} year is not leap year".format(year)