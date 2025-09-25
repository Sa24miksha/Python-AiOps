Sets

Catchy Point: “Unique, Unordered, Mutable”

When to use:

Removing duplicates from list

Membership testing (fast!)

Set operations → union, intersection, difference

we use { } this identify or use Sets 


# Set operations
a = {1,2,3}
b = {2,3,4}
print(a | b)  # Union → {1,2,3,4}
print(a & b)  # Intersection → {2,3}
print(a - b)  # Difference → {1}


Difference between remove() and discard() in sets

remove(value) → removes the value, throws error if value not present

discard(value) → removes the value, does NOT throw error if value not present

clear() → removes all elements from the set

Catchy tip:

remove = strict

discard = safe