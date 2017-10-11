import re

data = open("regex_sum_31737.txt")
y= data.read()
x = re.findall('[0-9]+',y)

int_lst= []
for each in x:
	z= int(each)
	int_lst.append(z)


print("Sum of Numbers:", sum(int_lst))
