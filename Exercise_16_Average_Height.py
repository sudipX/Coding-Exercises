# Average Height Calculator

student_heights = input("Enter the list of student heights:\n>> ").split()


for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

# Finding total sum of individual heights in the list
sum_of_heights = 0

for height in student_heights:
    sum_of_heights += height

#print(sum_of_heights)

# Finding total number of students in the list
total_no_of_students = 0

for student in student_heights:
    total_no_of_students += 1

#print(total_no_of_students)

# Calculating average height
average_height = round(sum_of_heights / total_no_of_students)

print(f"Average height : {average_height}")