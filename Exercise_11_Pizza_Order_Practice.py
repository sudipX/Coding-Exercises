# Python Pizza Order
print("Welcom to Python Pizza Deliveries !")
size = input("Enter the size of pizza you want:\nS > small\nM > medium\nL > large\n:").lower()
add_pepperoni = input("Add pepperoni:\nY > yes\nN > no\n:").lower()
add_extra_cheese = input("Add extra cheese:\nY > yes\nN > no\n:").lower()
final_bill = 0

if add_extra_cheese == "y":
    final_bill += 1
if add_pepperoni == "y":
    if size == "s":
        final_bill += 2
    else:
        final_bill += 3
if size == "s":
    final_bill += 15
elif size == "m":
    final_bill += 20
else:
    final_bill += 25

print(f"Your final bill is ${final_bill}. Enjoy !!!")