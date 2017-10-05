# Python Program to find the area of triangle

a, b, c = 5, 6, 7

# Calulate the sami parameter of triangle
s = (a + b + c) / 2

# Calculate the area
area = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2.0)

print "Area of triangle is : {:.2f}".format(area)
