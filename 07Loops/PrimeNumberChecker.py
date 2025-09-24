number = int(input("Enter the number: "))
is_prime = True

if number > 1:
    for i in range(2, number):  #here number+1 not done because the rimeno. is divisible by its self
        if (number%i) == 0:
            is_prime = False
            break

print(is_prime)