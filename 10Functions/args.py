# functions with *args - 
# write a function that takes varibale number of arguments and return there sum - 

# def sum_all(*args):
#     return sum(args)

# print(sum_all(1,2))
# print(sum_all(1,2,3,4,5))
# print(sum_all(1,2,3,4,5,6,7,8,9))

# * -> expect multiple arguments 
# we can also print args as 

def sum_all(*args):
    print(*args) #return parameters along with the sum 
    #print(args) #return a tuple with comma seperated parameters and the sum 
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,4,5,6,7,8,9))
