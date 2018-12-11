#10/12/2018
#Assignment 25: Accept a string and display the resultant string in reverse order. The resultant string should contain all characters at the
#	even position of accepted string ignoring blank spaces.

string = input("Enter a string:")
res = ""
for i in string:
	if i not in " ":
		res+=i

resultant = ""
for i in range(0,len(res)+1,2):
	resultant+=res[i]

print("Resultant String:",resultant)

output = ""
for j in range(1,len(resultant)+1):
	output+=resultant[-j]
print("Output String:",output)
