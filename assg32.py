#10/12/2018
#Assignment 32: Sorting given currency in descending order of denominations

currency = [4,1,6,2,8,5]

for i in range(0,len(currency)-1):
	for j in range(0,len(currency)-1):
		if currency[j]>currency[j+1]:
			t = currency[j]
			currency[j] = currency[j+1]
			currency[j+1] = t
#asc = []
des = []

for k in range(0,len(currency)):
	#asc.append(currency[k])
	des.append(currency[-(k+1)])
	
print("Sorted:")
#print(asc)
print(des)
