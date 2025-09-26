def greet(name):
    return "hey " + name 

greetings = greet("samiksha")
print(greetings)

# Types of Arguments

# Positional arguments
def add(num1, num2):
    return num1 + num2

print(add(5,2))

# Default arguments
def sayHey(name="Samiksha"):
    print(f"Greetings {name}")

sayHey()

# Keyword arguments
def info(name, age):
    return f"{name} is {age} years old!"

print(info(age=22, name="Anchat"))

# Variable-length arguments
def addNums(*args):
    return sum(args)

print("The sum is:", addNums(1,2,3,4,5))


# Keyword variable-length arguments

def StudentInfo(**kwargs):
    return kwargs

print(StudentInfo(name="Riyansh", age=22, Address="Shahdol"))