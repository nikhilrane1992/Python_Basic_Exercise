# Python program to check if the number provided by the user is an
# Armstrong number or not


# Method 1
num = raw_input("Enter a number: ")
n, t_sum = len(num), 0

for i in num:
    t_sum += int(i) ** n

if t_sum == int(num):
    print "{} is armstrong".format(num)
else:
    print "Number is not armstrong"

print "-" * 20

# Method 2
num = int(raw_input("Enter a number: "))
tmp, t_sum, n = num, 0, len(str(num))

for i in range(n):
    digit = tmp % 10
    t_sum += digit ** n
    tmp //= 10

if t_sum == num:
    print "{} is armstrong".format(num)
else:
    print "Number is not armstrong"
