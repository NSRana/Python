#10/12/2018
#Assignment 16: Calculating income tax and the net salary of employee based on their gross salary

employee_id = 1001
basic_sal = 15000.00
allowance = 6000.00
gross_sal = basic_sal + allowance
if gross_sal >20000:
	income_tax = gross_sal*30/100
elif gross_sal >10000 and gross_sal <= 20000:
	income_tax = gross_sal*20/100
elif gross_sal >10000 and gross_sal <=5000:
	income_tax = gross_sal*10/100
else:
	income_tax = 0
net_sal = gross_sal - income_tax
print("Employee Id:",employee_id)
print("Basic Salary:",basic_sal)
print("Allowances:",allowance)
print("Gross Pay:",gross_sal)
print("Income Tax:",income_tax)
print("Net Pay:",net_sal)
