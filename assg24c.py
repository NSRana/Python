#10/12/2018
#Assignment 24c: Calculate the number of vowels in a string

string = input("Enter a String:")
count=0
for i in string:
	if i.upper() in "AEIOU":
		count+=1
print(count)
