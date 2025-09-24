import math
# Basic function syntax
# write a function that return a sqaure of any number 

def findSqaure(num):
    return num*num

print(f"The sq. is: ")
print(findSqaure(5))


# Function with multiple parameters -

def add_Two(num1, num2):
    print(num1 + num2)

add_Two(5,5)   

# Write a function multiply that multiplies two number but can also expect multiple strings

def multiply(num1, num2):
    return num1 * num2

print(multiply(8,5))
print(multiply('h', 5))
print(multiply(5,'h'))

# write a function that return both area and circumference of the circle 

# def circle_stats(radius):
#     return math.pi * radius ** 2
#     print("hi")

# print("Area of circle is: " , circle_stats(6))
# The execution will stops as you write the return keyword, the print statement will never be printed 

# thus we will hold the area in a varibale because after return execution stops as - 
# using round - 


# def circle_stats(radius):
#     area =  math.pi * radius ** 2
#     circumference = 2 * math.pi * radius
#     return round(area,2), round(circumference,2)

# a,c = circle_stats(2)

# print('Area:' , a , 'Circumference:', c)



# either using tring formating - 
def circle_stats(radius):
    area =  math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a,c = circle_stats(2)

print(f"Area: {a:.2f} Circumference: {c:.2f}")

# write a function that greet a user, if no name is provided, it should greet with default name

def greet(name = "user"):
    print("hello" , name, "!")

greet("samiksha")
greet()

