# Love Calculator
print("THE LOVE CALCULATOR")
name1 = input("Enter your name:\n").lower()
name2 = input("Enter your partner name : \n").lower()

combined_name = name1 + name2

t_count = combined_name.count("t")
r_count = combined_name.count("r")
u_count = combined_name.count("u")
e_count = combined_name.count("e")

true = str(t_count + r_count + u_count + e_count)

l_count = combined_name.count("l")
o_count = combined_name.count("o")
v_count = combined_name.count("v")

love = str(l_count + o_count + v_count + e_count)

love_percentage = int(true + love)

if love_percentage <= 10 or love_percentage > 90:
    print(f"You love score is {love_percentage}. You go together like coke and mentos.")
elif love_percentage >= 40 and love_percentage <= 50:
    print(f"Your love score is {love_percentage}. You are alright together.")
else:
    print(f"You love score is {love_percentage}.") 