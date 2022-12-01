# Paint area calculator

height_of_wall = int(input("Height of the wall: \n>> "))
width_of_wall = int(input("Width of the wall: \n>> "))
can_coverage = int(input("Per Can Coverage: \n>> "))

def paint_area_calculator(height, width, coverage):
    number_of_cans_required = round((height * width) / coverage)
    print(f"No. of cans required: {number_of_cans_required}")

paint_area_calculator(height=height_of_wall, width=width_of_wall, coverage=can_coverage)