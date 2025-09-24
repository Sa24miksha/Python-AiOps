tea_varity = ["Green", "Black", "Oolong", "White"]
print(tea_varity)

# accessing valued with indexes 
print(tea_varity[0])
print(tea_varity[2])
print(tea_varity[-1])

# slicing and dicing 
print(tea_varity[1:4])
print(tea_varity[2:])
print(tea_varity[:3])

# updating 
tea_varity[3] = "Herbal"
print("updated: " , tea_varity)

#surprise
#tea_varity[1:2] = "Lemon"
#print(tea_varity) #['Green', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal'] the value will be inserted as an array 
# to fix this we will pass the value of as an array as follows 


tea_varity[1:2] = ["lemon"]
print(tea_varity)

tea_varity[1:3] = ["yellow", "masala"]
print(tea_varity)

# print the list 
print("Printing tea: ")
for tea in tea_varity:
    print(tea)

# printing with -
print("Printing with -")
for tea in tea_varity:
    print(tea, end="-")

# checking if present
if "Herbal" in tea_varity:
    print("Herbal is present")


#  adding in the end 
tea_varity.append("Oolong")
print(tea_varity)

# pop vs remove 
print("pop:")
tea_varity.pop() #when used in terminal, it omit the output 


tea_varity_copy = tea_varity.copy()
tea_varity_copy.append("Applays")
print(tea_varity)
print(tea_varity_copy)
