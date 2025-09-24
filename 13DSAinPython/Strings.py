s = "Hello Python"
print(s[0])       # H (indexing)
print(s[-1])      # n (last character)
print(s[0:5])     # Hello (slicing)
print(s.upper())  # HELLO PYTHON
print(s.lower())  # hello python
print(s.replace("Python", "Samiksha"))  # Hello Samiksha


# Definition:

# Text data ko represent karte hain.
# Immutable (directly change nahi kar sakte).
# mportant String Methods:

s = "hello python"

print(s.upper())        # HELLO PYTHON
print(s.lower())        # hello python
print(s.title())        # Hello Python
print(s.capitalize())   # Hello python
print(s.strip())        # removes whitespace
print(s.replace("python", "Samiksha"))  # hello Samiksha
print(s.split())        # ['hello', 'python']
print("-".join(["hello", "python"]))  # hello-python
print(s.find("python"))  # 6 → index of substring
print(s.count("o"))     # 2 → count occurrences