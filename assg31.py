#10/12/2018
#Assignemnt 31: Generating first 'n' Fibonacci numbers in a list

L = []
L.insert(0,0)
L.insert(1,1)
n=int(input("Enter n:"))
for i in range(2,n):
	L.insert(i,L[i-1]+L[i-2])

print(L)
