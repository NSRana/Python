#11/12/2018
#Assignment 29: Printing required information stored in tuples in Student Management System

courses = ('Python Programming', 'RDBMS', 'Web Technology', 'Software Engg')
electives = ('Business Intelligence', 'Big Data Analytics')

#a.
print("Number of courses opted by John:",len(courses))

#b.
print("Courses opted by John:")
for i in courses:
	print(i)

#c.

updated_courses = courses + electives
print("Updated course list:")
for j in updated_courses:
	print(j)
	
#d.
#Change not possible, because tuples are immutable
