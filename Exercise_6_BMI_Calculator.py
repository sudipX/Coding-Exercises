# BMI CALCULATOR
print("BMI CALCULATOR")
weight = float(input("Enter Your Weight (kg):\n"))
height = float(input("Enter Your height (m):\n"))

bmi = str(int(weight/height**2))
print("Your BMI is " + bmi)