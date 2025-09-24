print("Normal function: ")
def norm_fun():
    return 1
    return 2
    return 3
ans1 = norm_fun()
print(ans1)
print(ans1) #this never execute 
print(ans1)

print("Yield Function: ")
def yield_fun():
    yield 1
    yield 2
    yield 3
ans2 = yield_fun()
print(next(ans2))
print(next(ans2))
print(next(ans2))
