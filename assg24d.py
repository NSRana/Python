#10/12/2018
#Assignment 24d: Remove the punctuations from the string

string = input("Enter a string:")
punct = "!()-[]{};:'\"\,<>./?@$%^&*#_~"
res = ""
for i in string:
	if i not in punct:
		res+=i
print(res)
