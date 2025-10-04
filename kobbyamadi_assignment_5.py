print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: "))
step_count = 0

print("Sequence:", end=" ")
print(current_number, end=" ")

while current_number != 1:
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = current_number * 3 + 1
    print(current_number, end=" ")
    step_count += 1

print("Steps:", step_count)

print("=== Challenge 2: Prime Number Checker ===")
number = int(input("Enter a number: "))

if number <= 1:
    print("Please enter a number greater than 1.")
else:
    print(f"Testing divisors from 2 to {number - 1}")
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not prime (divisible by {i})")
            is_prime = False
            break
    if is_prime:
        print(f"{number} is prime!")
print()

print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")

print("    ", end="")  
for col in range(1, 11):
    print(f"{col:4}", end="")
print()

for row in range(1, 11):
    print(f"{row:2}  ", end="") 
    for col in range(1, 11):
        product = row * col
        print(f"{product:4}", end="")
    print()
