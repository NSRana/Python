#10/12/2018
#Assignment 24a: Calculate the number of capital letters in a string

str=input("Enter a string:")
count=0
for i in str:
	if i.isupper():
		print(i)
		count+=1
print("Total:",count)
