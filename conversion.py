# Convert kilometers to mile
# To take kilometers from the user
km = input("Enter value in kilometers: ")

# conversion factor for km to mile
conv_fac = 0.621371

# calculate miles
miles = km * conv_fac
print '{:.3f} kilometers is equal to {:.3f} miles'.format(km, miles)


# Python Program to convert temperature in celsius to fahrenheit

# change this value for a different result
celsius = input("Enter value in celsius: ")

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print '{:.1f} degree Celsius is equal to {:.1f} degree Fahrenheit'.format(
    celsius, fahrenheit)
