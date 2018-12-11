#10/12/2018
#Assignment 20: a)Correct the code to print even numbers between 50 and 80(both inclusive)
#               b)Write a code for the same using while loop

for i in range (50, 81):
	if i % 2 == 0:
		print(i)

j=50		
while j<=80:
	if j % 2 == 0:
		print(j)
	j+=1
