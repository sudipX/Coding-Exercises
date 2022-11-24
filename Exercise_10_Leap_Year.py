# Leap Year 
print("CHECK LEAP YEAR")
year_input = int(input("Enter the year you want to check:\n"))

if year_input % 4 == 0:
    if year_input % 100 == 0:
        if year_input % 400 == 0:
            print("Leap Year.")
        else:
            print("Not a Leap Year.")
    else:
        print("Leap Year.")
else:
    print("Not a Leap Year.")