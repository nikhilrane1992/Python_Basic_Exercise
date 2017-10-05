# Python program to check if the input number is prime or not

# take input from the user
num = int(input("Enter a number: "))

for i in range(2, num):
    if (num % i) == 0:
        print "{} number is not prime".format(num)
        break
else:
    print "{} number is prime".format(num)
