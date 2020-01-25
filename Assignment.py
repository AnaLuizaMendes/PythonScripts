#Assignment 1:
#Student Grades Program.

#Ask how many students to calculate
#Take in X number of grades
#Output: Highest, Lowest and Average Grade.


students_number = input('How many students do you teach? ')
student_grades = []
i = 0

for each in range(int(students_number)):
    student_grades.append(int(input('What is the student ' + str(i + 1) + ' grade? ')))
    i += 1

# how to find the highest and lowest numbers
student_grades.sort()
print('The highest grade in your class is ' + str(student_grades[0]))
print('The lowest grade in your class is ' + str(student_grades[-1]))

# how to find the middle index of the list
print('The middle number in your Student Grade list is ' + str(student_grades[int(len(student_grades)/2)]))

# how to find the average number in a list
average_grade = sum(student_grades)/len(student_grades)
print('The Average Grade in your class is ' + str(average_grade))

