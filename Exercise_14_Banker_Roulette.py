# Banker_Roulette
import random
print("Who is going to pay the bill ?")

names_input = input("Enter everybody's name:\n(Please consider using comma and space for name separation)\n> ")

list_of_names = names_input.split(", ")
# print(list_of_names)

length_of_list = len(list_of_names)
# print(length_of_list)
random_index = random.randint(0, length_of_list-1)
# print(random_index)

payer_name = list_of_names[random_index]

print(f"{payer_name.capitalize()} is going to pay the bil.")
