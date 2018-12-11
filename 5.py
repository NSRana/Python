import math
n=int(input("Enter a number:"))
for i in range(2, int(math.sqrt(n))+1):
	if n % i == 0:
		print("Not Prime")
	else:
		print("Prime")
