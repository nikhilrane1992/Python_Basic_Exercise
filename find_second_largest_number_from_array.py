# find out second largest number from list
array = [1, 5, 6, 7, 3, 4, 5, 6, 3, 1, 43, 43, 42, 42, 42, 3, 5, 7, 8, 9, 5, 3]
# Method 1
print sorted(set(array))[-2]


# Method 2
a, b = 0, 0
for i in array:
    if i > a:
        b, a = a, i
    elif a > i > b:
        b = i
print b
