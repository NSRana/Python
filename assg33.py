#10/12/2018
#Assignment 33: Generating valid bill for furniture store

furniture=[["Sofa Set",20000],["Dining Table",8500],["T.V. Stand",4599],["Cupboard",13920]]
item = input("Enter the furniture to be purchased:")

amt = 0
flg = 0
for i in furniture:
	if item.upper() == i[0].upper():
		flg=1
		amt+=i[1]
		break
if flg == 1:
	print("Total payment:", amt)
else:
	print("Item not Available")
