# Create a tuple t with 5 numbers and find index of the number 3.

t = (1,8,5,6,7,4,3,9)

print(t.index(3))


# 2. Remove duplicates from list [1,2,3,2,4,1,5] using set.

li = [1,2,3,2,4,1,5]
st = set(li)
print(st)

# Create a dictionary person with keys: name, age, city and print all keys.

person = {
    "name":"Samiksha",
    "age": 22,
    "city":"Shahdol"
}

print(person.keys())
print(person.values())
print(person)

# Write a ternary statement to assign "Adult" if age >= 18, else "Minor".

bd = 16
ans = "Adult" if bd >= 18 else "Minor"
print(ans)

# What will this print?

# for i in range(5):
#     if i == 2:
#         continue
#     print(i)



# KEY TAKEAWAYS - 
# keys() and values() need parentheses.

# range(n) starts from 0 by default.

# Sets are unordered.




