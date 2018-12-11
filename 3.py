max_marks=50
mark1 = int(input("Enter marks for Sub1:"))
mark2 = int(input("Enter marks for Sub2:"))
mark3 = int(input("Enter marks for Sub3:"))
mark4 = int(input("Enter marks for Sub4:"))
mark5 = int(input("Enter marks for Sub5:"))
avg = (mark1 + mark2 + mark3 + mark4 + mark5)/5
print("Average marks:",avg)
percent = avg*100/max_marks
if percent >= 80:
	print("Grade: A")
elif percent > 65 and percent <= 80:
	print("Grade: B")
elif percent > 50 and percent <= 65:
	print("Grade: C")
elif percent > 33 and percent <= 50:
	print("Grade: D")
else:
	print("Fail")
