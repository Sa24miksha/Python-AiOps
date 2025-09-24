# Compute factorial using while loop 

number = 5
factorial = 1

while number > 0:
    factorial = factorial * number
    number = number - 1

print(f"Factorial is: ", factorial)