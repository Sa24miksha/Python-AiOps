# Create a function  that accepts any number of keywprd rguments and print them in the fprmat key:value

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_kwargs(name="Samiksha", age="24")
print_kwargs(name="Riyansh", age="22", proffession="student")
print_kwargs(name="Anchat")