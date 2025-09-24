chai_types = {"Ginger" : "Zesty",
              "Lemon" : "Citric",
              "Green" : "Mild"}
print(chai_types)

# accessing values with keys 
print(chai_types["Ginger"])

chai_types.get("Ginger") 

# change the values 
chai_types["Green"] = "Fresh"
print(chai_types)

# printing keys only 
for chai in chai_types:
    print(chai)

# printing values along with keys 
for i in chai_types:
    print(i, chai_types[i])

# another method to print key and value is using .items()
for key, value in chai_types.items():
    print(key, value)

# check if value is present or not - 
if "Ginger" in chai_types:
    print("i have Ginger in my chai !")

# find the length of the dictionary 
print(len(chai_types))

# inserting a key and value pair 
chai_types["Earl grey"] = "Sweet"
print(chai_types)

# pop - have to provide the keys unlike "List", omit the popped item in terminal
chai_types.pop("Lemon")
print(chai_types)

# popitem - no parametere to pass cause it would remove the last item from te dictionary, wont omit anything
chai_types.popitem()
print(chai_types)

# del - also delete by key , delete the refernec from the memory 
del chai_types["Green"]
print(chai_types)

# create a copy with different reference 
chai_types_copy = chai_types.copy()
chai_types_copy["cinamon"] = "Spicy"
print("original: ", chai_types)
print("copy: ",chai_types_copy)


# nested dictionary 
cafe_shop = {
    "tea" : {"Ginger" : "Spicy", "Green" : "Mild"},
    "coffee": {"Capechino": "Strong", "Latte": "Milk"}
}
print(cafe_shop)

# accessing values of the nested dictionary - level 01
print(cafe_shop["tea"])

# accessing values of the nested dictionary - level 01
print(cafe_shop["tea"]["Ginger"])


# QUESTIONS - 
# Squared of any no stored as key and val
squared_number = {x:x**2 for x in range(10)}
print(squared_number)

cube_number = {x: x**3 for x in range(10)}
print(cube_number)

# constructing a dictionary from keys array and default values - 
keys = ["Apple", "Banana", "Mango", "Organe"]
default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)