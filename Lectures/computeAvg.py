'''
Write a program that reads the grades of students in a class, and prints the average.
'''

# students_in_class = int(input("Enter number of students: "))
#
# total_sum_of_students_grades = 0
#
# print("Enter the students grades (in separate lines):")
# for _ in range(students_in_class):
#     student_grade = int(input())
#     total_sum_of_students_grades += student_grade
#
# print("The average grade for students is:", total_sum_of_students_grades / students_in_class)


'''
Write a program that reads a sequence of grades (till 'done' is entered), and prints the average.
'''
seen_done = False
grades_sum = 0
students_count = 0

print("Enter the students grades in separate lines, to end the input type 'done':")
while (not seen_done):
    curr_input = input()
    if (curr_input == 'done'):
        seen_done = True
    else:
        student_grade = int(curr_input)
        students_count += 1
        grades_sum += student_grade
print("The average class grade is: ", grades_sum / students_count)