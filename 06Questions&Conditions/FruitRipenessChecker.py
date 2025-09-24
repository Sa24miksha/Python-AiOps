# Determine if a fruit is ripe , overripe or unripe based on it color
# eg, Banana:Green - unripe , Yellow - Ripe, Brown - overripe

fruit = input("Enter your fruit: ")
color = input("What is the color of your fruit? ")

if color == "Green":
    type = "Unripe"
elif color == "Yellow":
    type = "Ripe"
else:
    type = "Overripe"

print(f"{fruit} is:", type)