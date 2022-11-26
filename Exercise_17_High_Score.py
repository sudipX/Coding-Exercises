# Highest Score from the list

student_scores = input("Enter the list of student heights:\n>> ").split()


for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(student_scores)

# Finding highest score from the list

highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"Highest Score : {highest_score}")