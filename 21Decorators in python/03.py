# Cache return value 
# Implement the decorator that caches the return value of a function so that when its called iwththe 
# same arguments the cached value is returned instead of re-executing the function .

import time

def cache(fun):
    cache_val = {}
    def wrapper(*args):
        if args in cache_val:
            return cache_val[args]
        result = fun(*args)
        cache_val[args] = result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a+b

print(long_running_function(2,3))
print(long_running_function(2,3)) #after 4 sec
print(long_running_function(5,5)) #after next 4 sec


