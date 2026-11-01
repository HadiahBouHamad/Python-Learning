num = input("Enter a number: ")
check = input("Enter a number to check divisibility: ")
num = int(num)
check = int(check)
if num % 4 == 0:
    print(f"The number {num} is even and a multiple of 4.")
elif num % 2 == 0:
    print(f"The number {num} is even.")
else:
    print(f"The number {num} is odd.")

def is_evenly_divisible(num, check):
    if check == 0:
        print("Cannot divide by zero.")
    elif num % check == 0:
        print(f"The number {num} is evenly divisible by {check}.")
    else:
        print(f"The number {num} is not evenly divisible by {check}.")

is_evenly_divisible(num, check)