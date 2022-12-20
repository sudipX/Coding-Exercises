# Grading Program

student_scores = {
    "Sudeep" : 99,
    "Aayusha" : 98,
    "Rajesh" : 81,
    "Ashutosh" : 78,
    "Srijan" : 62,
    "Biswash" : 74 
}

student_grades = {}

for students in student_scores:
    grade = ""
    score = student_scores[students]
    if 91 <= score <= 100:
        grade = "Outstanding"
    elif 81 <= score <= 90:
        grade = "Exceeds Expectation"
    elif 71 <= score <= 80:
        grade = "Acceptable"
    elif score <= 70:
        grade = "Fail"
    student_grades[students] = grade

print(student_grades)