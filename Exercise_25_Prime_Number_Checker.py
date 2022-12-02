# Prime Number Checker

number = int(input("Enter the number:\n>> "))


def check_prime(n):
    isPrime = True
    if n == 1 or n == 2:
        isPrime = True
    if n > 2:
        for number in range(2, n):
            if n % number == 0:
                isPrime = False
    
    if isPrime == True:
        print("Prime Number")
    elif isPrime == False:
        print("Not a Prime Number")
    
check_prime(number)