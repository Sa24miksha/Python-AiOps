# Tuples - immutable , ()

Fruits = ("Apple", "Banana", "Mango", "Organe", "Grapes")
print(Fruits)

print(Fruits[0])
print(Fruits[1:])
print(Fruits[-1])


# ERROR!! - CANNOT BE MODIFIED , IMMUTABE 
# Fruits[0] = "papaya"
# print(Fruits) 


more_fruits = ("Kiwi", "Avacardo","Peach")
all_fruits = more_fruits + Fruits
print(all_fruits)


# IMPORTANT - tuples are used to unwrap tuples !
# ss attaced 

# Find the type 
print(type(Fruits))