# Treasure Map
row1 = ["#", "#", "#"]
row2 = ["#", "#", "#"]
row3 = ["#", "#", "#"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want ot put the treasure ?")

# Taking hold of the horizontal position
row_position_hold = int(position[0])
row_hold = map[row_position_hold - 1]

#Taking hold of th vertical position
column_position_hold = int(position[1])
row_hold[column_position_hold - 1] = "$"


print(f"{row1}\n{row2}\n{row3}")