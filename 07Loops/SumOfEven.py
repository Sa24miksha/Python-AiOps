# sum of given even numbers 

number = [1,2,3,4,5,6,7,8,9,10,11,12]
even_sum = 0

for num in number:
    if num%2==0:
        even_sum += num

print("Sum of given even numbers is: ", even_sum)

# sum of first n even numbers

n = int(input("Give the value of n: "))  # convert input to int
total = 0

for i in range(1, n+1):   # loop from 1 to n
    if i%2==0:
        total += i       # even numbers are 2,4,6... = 2*i

print("Sum of first", n, "even numbers is:", total)

