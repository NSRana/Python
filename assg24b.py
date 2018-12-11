#10/12/2018
#Assignment 24b: Check if the entered string is palindrome or not

string = input ("Enter a string:")
flag = 1
for i in range(0, int(len(string))):
	if string[i] != string[-(i+1)]:
		print("Not a Palindrome")
		flag = 0
		break
if flag == 1:
	print("Is a Palindrome")
