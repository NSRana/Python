#10/12/2018
#Assignment 35: Generate output for required conditions using sets

java_course = {'John', 'Jack', 'Jill', 'Joe'}
python_course = {'Jake', 'John', 'Eric', 'Jill'}

#a.
print("Number of students enrolled in Python course: ", len(python_course))

#b.
print("Number of students enrolled in Java course only: ", len((java_course-python_course)))

#c.
print("Number of students enrolled in Python course only: ", len((python_course-java_course)))

#d.
print("Number of students enrolled for both Java and Python courses: ", len((python_course & java_course)))
print(python_course & java_course)

#e.
print("Number of students enrolled for either Java or Python but not both courses: ", len((python_course ^ java_course)))
print(python_course ^ java_course)

#f.
print("Number of students enrolled for either Java or Python courses: ", len((python_course | java_course)))
print(python_course | java_course)
