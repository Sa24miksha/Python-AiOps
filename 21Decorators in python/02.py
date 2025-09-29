# Debugging Function Calls 
# Crete a decorator to print the function  name and the value of its arguments everytime the function
# is called !

def debug(fun):
    def wrapper(*args, **kwargs):
        
        args_val = ", ".join(str(arg)  for arg in args)
        kwargs_val = ", ".join(f"{k} = {v}" for k,v in kwargs.items())
        print(f"Calling {fun.__name__} with args value: {args_val} and kwargs value: {kwargs_val}")

        return fun(*args, **kwargs)
    
    return wrapper


@debug
def greet(name, greeting="hello"):
    print(f"{greeting} {name}")

greet("Samiksha", greeting="Hiieee")