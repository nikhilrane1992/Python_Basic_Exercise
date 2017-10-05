# Program to display the Fibonacci sequence up to n-th

n = int(input("Enter number: "))

num1, num2, count, x = 1, 1, 1, 0

while count <= n:
    print num1
    x = num1 + num2
    num1 = num2
    num2 = x
    count += 1


# Fibonacci series by recursion method

def fab(x):
    if x <= 1:
        return x
    else:
        return (fab(x - 1) + fab(x - 2))


for i in range(1, n + 1):
    print fab(i)
