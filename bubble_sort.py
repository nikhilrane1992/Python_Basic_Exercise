# Sort input list in ascending order using bubble sort

input_list = [2,5,6,3,4,9,5,2,33,66,33,88,99,2,56]

for i in range(len(input_list)):
    for j in range(0, i):
	if input_list[i] < input_list[j]:
    	    input_list[i], input_list[j] = input_list[j], input_list[i]

print input_list
