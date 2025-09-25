# Numbers 
a = 10
print(type(a))

b = 5.90
print(type(b))

c = 2 + 4j
print(type(c))


# sequence 
# 1. String
s1 = "Samiksha"
print(s1)
print(type(s1))
print(s1[-1])

s2 = 'a'
print(type(s2))


# 2. List - ordered, mutable, mixed data allowed 
# we use [] brackets 
l1 = ["epam", 10, 'july', 3.0, 2.9]
print(l1[2])


# 3. Typle - ordered , immutable 
#  we use () parenthesis 
t1 = ("apple", "ball", 24, 'abc')
print(t1[1])


# Boolean 
print(15 > 9)
print(2 == '2')


# Set - unordered, unique element only, mutable 
# we use {} curly braces 
st = {"logo", 12, "cartoon", 29, 36.575, "logo", 12}
print(st)
# print(st[2])


# frozen set - immutable set 
fs = ([3,4,51,2,3,4,5,6,7,8,8])
print(fs)

# Mapping - Dict , ordered, unique keys 
student = {
           "name" : "Aryan",
           "class": 12,
           "section": 'C',
           4 : 5.11
        }
print(student)
print(student["section"])
print(student[4])
print(student.get("name"))


# learning about references - 
myListOne = [1,2,3,4]
myListTwo = myListOne

myListOne = [1,2,3]
myListOne[0] = 99

print(myListOne)
print(myListTwo)


# format 
firts_name = "Samiksha"
last_name = "yadav"

print("The first name is {} and the last name is {}".format(last_name, firts_name))

# when ypou want to set a particular ordering for the values use this
print("The first name is {first} and the last name is {last}".format(first=firts_name,last=last_name))

# find the length 
print(len('_samiksha.haha'))

# find the types 
print(type("hola"))
print(type(537654))
print(type(653.867))
print(type([1,2,a,b,c,"sam"]))


# concatination - 
num = "100"
print(int(num) + 5)
