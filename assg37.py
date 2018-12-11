#10/12/2018
#Assignment 37: Identifying top three scorers and calculating average marks using dictionary

import operator
score = {"John":86.5, "Jack":91.2, "Jill":84.5, "Harry":72.1, "Joe":80.5}

sorted_list = sorted(score.items(), key = operator.itemgetter(1), reverse = True)

print("\nTop three scorers:")

c = 0
for student in sorted_list:
	if c == 3:
		break
	print(student)
	c += 1

total = sum(score.values())

avg = total / len(score)
print("\nAverage Score: ",avg)
