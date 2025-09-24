import copy

# Shallow copy - 

original = [1, 2, 3]
shallow = copy.copy(original)

shallow.append(4)
print("Shallow with lists: -")
print(original)
print(shallow)

print(original is shallow)

# problem with nested list - 

list_01 = [[1,2],[3,4]]
list_02 = copy.copy(list_01)

list_02[0].append(6)

print("Shallow with nested lists: -")
print(list_01)
print(list_02)


# Deepcopy - 
list1 = [[1,2],[3,4]]
list2 = copy.deepcopy(list1)

list2[0].append(6)

print("DeepCopy with nested lists: -")
print(list1)
print(list2)





