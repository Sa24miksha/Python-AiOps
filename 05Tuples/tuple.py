# Tuples - immutable , ()

Fruits = ("Apple", "Banana", "Mango", "Organe", "Grapes")
print(Fruits)

print(Fruits[0])
print(Fruits[1:])
print(Fruits[-1])

# concatination in tuple 
a = (1,2,4)
b = (5,6,7)
ans = a + b
# or
ans2 = (1,2,4) + (5,6,7)
print("Concatination 1: " , ans)
print("Concatination 2: " , ans2)


# repetition - 
printHi = ("hi", )*3
print("repetition - ",  printHi)


lengthOfTup = (0.3,4.6,9.0,8.0)
print("Printing length -",len(lengthOfTup))


# ERROR!! - CANNOT BE MODIFIED , IMMUTABE 
# Fruits[0] = "papaya"
# print(Fruits) 


more_fruits = ("Kiwi", "Avacardo","Peach")
all_fruits = more_fruits + Fruits
print(all_fruits)


# IMPORTANT - tuples are used to unwrap tuples !
print("Unwrapping tuple- ")
person = ("samiksha", 22, "Bhopal")
name, age, city = person
print(name)
print(age)
print(city)

# Very useful in returning multiple values from a function:

def get_min_max(nums):
    return (min(nums), max(nums))

low, high = get_min_max([10, 2, 30, 4])
print(low, high)  # 2 30

# swap two numbers using tuples
a, b = 10, 20
a, b = b, a
print("Swapped-", a, b)


# Find the type 
print(type(Fruits))

# Can a Tuple contain Mutable Objects?
# Tuple comtaining mutable list - 
t = (1,2,[3,4])
print("original tuple", t)

t[2].append(5)
print("Modified tuple: ", t)