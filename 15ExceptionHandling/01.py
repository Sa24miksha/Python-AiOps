try:
    a = 10
    b = 0
    result = a/b
except ZeroDivisionError:
    print("The number when divided with zero will give the error")
finally:
    print("the end - 1")


#----------------------------------  Catching different types of exception -------------------------- 

try:
    num1 = int("Hello")
    num2 = 10/0
except ValueError:
    print("This is not a number")
except ZeroDivisionError:
    print("The number when divided with zero will give the error")
finally:
    print("The end  - 2!")


# If you want both exceptions checked, you need two separate try blocks or handle them together.

# 🌸 Example with Both Exceptions
try:
    num1 = int("Hello")
except ValueError:
    print("This is not a number")

try:
    num2 = 10/0
except ZeroDivisionError:
    print("The number when divided with zero will give the error")

finally:
    print("The end again!")


# ✅ Output:

# This is not a number
# The number when divided with zero will give the error
# The end again!

#---------------------------------------------- Using else and finally-----------------------------------------
print("Using else and finally: ")

try:
    nums = int("100")
    print(nums/10)
except ZeroDivisionError:
    print("Division by zero not allowed.")
else:
    print("No error occoured!")
finally:
    print("the end - 3")


# -----------------------------------Raising Your Own Exception-------------------------------------


print("Raising Your Own Exception: ")
age= 16

try:
    if age < 18:
        raise ValueError("You are below the age criteria!")
    else:
        print("welcome onboard!")
except ValueError as e:
    print("Caught an error:", e)
finally:
    print("Done with age check ✅")


#------------------------------------------ Custom Exception---------------------------------------

# Step 1: Define your own Exception class
class MyError(Exception):
    pass


# Step 2: Use try-except with custom exception
try:
    raise MyError("This is my custom error!")

except MyError as e:
    print("Caught error", e)

finally:
    print("Custom exception check finished ✅")

    



