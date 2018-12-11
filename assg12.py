#10/12/2018
#Assignment 12: Calculate discounted bill based on appropriate conditions

bill_id = 1001
customer_id = 101
bill_amount = 199.99
print("Bill Id:%d" %bill_id)
print("Customer Id:%d" %customer_id)
print("Bill Amount:Rs.%0.2f" %bill_amount)
if bill_amount>500:
	bill_amount-=(bill_amount*2/100)
	print("Discounted Bill Amount:Rs.%0.2f" %bill_amount)
else:
	bill_amount-=(bill_amount*1/100)
	print("Discounted Bill Amount:Rs.%0.2f" %bill_amount)
