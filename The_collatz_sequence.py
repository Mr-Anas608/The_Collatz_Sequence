
def collatz(number):
    global steps
    steps = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        print(number)
        steps += 1


try:
    number = int(input("Enter a positive integer: "))
    if number<=0:
        raise ValueError("The number must be greater than zero")
    collatz(number)
except ValueError:
    print("Invalid input! Please enter a positive integer.")


print(f"\nSequence complete! After {steps} steps.")
