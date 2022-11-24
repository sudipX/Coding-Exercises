# BMI CALCULATOR
print("BMI CALCULATOR 2.0")
weight = float(input("Enter Your Weight (kg):\n"))
height = float(input("Enter Your height (m):\n"))

bmi = round((weight/height**2), 1)
if bmi < 18.5:
    print(f"Your BMI is {bmi}. You are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}. You have a normal weight.")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is {bmi}. You are overweight.")
elif bmi >= 30 and bmi < 35:
    print(f"Your BMI is {bmi}. You are obese.")
elif bmi > 35:
    print(f"Your BMI is {bmi}. You are clinically obese.")