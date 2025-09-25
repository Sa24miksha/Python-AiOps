# Definition:

# Unordered collection, no duplicates, mutable.
# Use { } brackets.

nums = {1, 2, 3, 3, 2}
print(nums)
nums.add(4)
nums.remove(2)
nums.discard(5)
print(len(nums))

# Set operations - 
a = {1,2,3}
b = {2,3,4}

print(a | b)  # Union → {1,2,3,4}
print(a & b)  # Intersection → {2,3}
print(a - b)  # Difference → {1}