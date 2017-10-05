# Python program to swap two variables

# To take input from the user
a, b = input('Enter value by comma seperated: ')

# create a temporary variable and swap the values
temp = a
a = b
a = temp

print('The value of a after swapping: {}'.format(a))

print('The value of b after swapping: {}'.format(b))


# Method 2 for swap the variable in python
a, b = b, a
print('The value of a after swapping: {}'.format(a))

print('The value of b after swapping: {}'.format(b))
