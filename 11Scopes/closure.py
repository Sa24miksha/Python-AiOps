#  Example 01 - 
# x = 99

# def fun(y):
#     z = x+y
#     return z

# print(fun(1))


# example - 2
x = 99
def func():
    global x
    x = 12

func()
print(x)


# example -03
X = 99
def f1():
    def f2():
        print(X)
    f2()
f1()


# closure - 
print("Closure - ")
def fun1():
    num = 24
    def fun2():
        print(num)
    return fun2

result = fun1()
result()


# closure 02 - 
print("closure in func-")

def func1(num1):
    def func2(num2):
        return num2 ** num1
    return func2

ans = func1(2) #num1
print(ans(3))  #num2