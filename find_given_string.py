# Find the given string in array
array = ['a', 'c', 'd', 'z', 'f', 'i', 'n', 'f', 'o', 'n', 'i']
f_str = 'info'

for i in range(len(array)):
    if ''.join(array[i:]).startswith(f_str):
        print "'{}' Found in array".format(f_str)
        break
else:
    print "Not found"


# Find the given string occurance in sentense

string = "azzcfdinfocfginfokmnvbinfo"
f_str = 'info'
count = 0

for i in range(len(string)):
    if string[i:].startswith(f_str):
        count += 1

print "No of '{}' occurance found in string '{}' is {}".format(
    f_str, string, count)
