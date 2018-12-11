#10/12/2018
#Assignment 13: Calculate discounted bill using appropriate conditions(if...else if ladder)

bill_id = 1001
customer_id = 101
bill_amount = 1990.99
print("Bill Id:%d" %bill_id)
print("Customer Id:%d" %customer_id)
print("Bill Amount:Rs.%0.2f" %bill_amount)
if bill_amount>=1000:
	bill_amount-=(bill_amount*5/100)
	print("Discounted Bill Amount:Rs.%0.2f" %bill_amount)
elif bill_amount>=500 and bill_amount<1000:
	bill_amount-=(bill_amount*2/100)
	print("Discounted Bill Amount:Rs.%0.2f" %bill_amount)
elif bill_amount>0 and bill_amount<500:
	bill_amount-=(bill_amount*1/100)
	print("Discounted Bill Amount:Rs.%0.2f" %bill_amount)
