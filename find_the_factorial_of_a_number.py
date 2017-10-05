# Python program to find the factorial of a number provided by the user.


# take input from the user
num = int(input("Enter a number: "))
fact = 1

if num < 0:
    print "Factorial not for negative numbers"
elif num == 1:
    print "Factorial of number {} is {}".format(num, num)
else:
    for i in range(1, num + 1):
        fact = fact * i

    print "Factorial of number {} is {}".format(num, fact)
