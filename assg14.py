#10/12/2018
#Assignment 14: Calculate the discount and put constraint on customer_id in Sales Retail Application

bill_id = 1001
customer_id = 101
bill_amount = 199.99
if customer_id>=101 and customer_id<=1000:
	print("Valid Customer")
	print("Bill Id:%d" %bill_id)
	print("Customer Id:%d" %customer_id)
	print("Bill Amount:Rs.%0.2f" %bill_amount)
	if bill_amount>=500:
		bill_amount-=(bill_amount*10/100)
		print("Discounted Bill Amount:Rs.%0.2f" %bill_amount)
else:
	print("Invalid Customer")
