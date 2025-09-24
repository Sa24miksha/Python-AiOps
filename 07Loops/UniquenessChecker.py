# Check if all the items in a list are unique, if a duplicate found exit the loop and print the duplicate 

items = ["Apple", "Banana", "Mango", "Apple", "Banana"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplocate: ", item)
        break
    unique_items.add(item)