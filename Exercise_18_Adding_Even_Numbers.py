# Adding Even Numbers using stepping
sum_of_all_evens = 0

for n in range(2, 101, 2):
    #print(n)
    sum_of_all_evens += n

print(f"Total sum: {sum_of_all_evens}")

# Alternate approach
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i

print(f"Sum: {sum}")