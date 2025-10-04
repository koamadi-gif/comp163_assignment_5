# USED GOOGLE GEMINI TO HELP DEBUG AND UNDERSTAND THE CODE
print("=== Challenge 1: Collatz Conjecture ===")

# User enters a number
current_number = int(input("Enter starting number: "))
step_count = 0

# Beginning of sequence
print("Sequence:", end=" ")
print(current_number, end=" ")

# Loop keeps going until the number is 1
while current_number != 1:
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = current_number * 3 + 1
    print(current_number, end=" ")
    step_count += 1

print("Steps:", step_count)

print("=== Challenge 2: Prime Number Checker ===")
# User enters a number
number = int(input("Enter a number: "))

# Checks if the number is less than or equal to 1
if number <= 1:
    print("Please enter a number greater than 1.")
else:
    print(f"Testing divisors from 2 to {number - 1}")
    prime = True
    # Loops through 2 to number - 1
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not prime (divisible by {i})")
            prime = False
            break # No need to check anymore
    # Number is prime if loop finishes without a divisor
    if prime:
        print(f"{number} is prime!")
print()

print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")

# Print column headers
print("    ", end="")  
for col in range(1, 11):
    print(f"{col:4}", end="")
print()

# Print each row of the multiplication table
for row in range(1, 11):
    print(f"{row:2}  ", end="") 
    for col in range(1, 11):
        product = row * col
        print(f"{product:4}", end="")
    print()


