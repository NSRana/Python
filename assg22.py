#10/12/2018
#Assignment 22: Putting constraint on the length of name of the customer

bill_id = input("Enter Bill id:")
customer_id = input("Enter Customer id:")
bill_amount = input("Enter Bill Amount:")
customer_name = input("Enter Customer Name:")
if ((len(customer_name) >= 3) and (len(customer_name) <= 20)):
	print("Bill Id: ",bill_id)
	print("Customer Id: ",customer_id)
	print("Bill Amount:Rs. ",bill_amount)
	print("Customer Name: ",customer_name)
else:
	print("Invalid customer name");

