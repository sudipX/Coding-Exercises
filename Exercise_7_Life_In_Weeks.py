# Life in Weeks
print("Life In Weeks")
age = int(input("Enter Your Age:\n"))
remaining_age = 90 - age

remaining_age_in_months = remaining_age * 12
remaining_age_in_weeks = remaining_age * 52
remaining_age_in_days = remaining_age * 365

print(f"You have {remaining_age_in_months} months, {remaining_age_in_weeks} weeks and {remaining_age_in_days} days left.")