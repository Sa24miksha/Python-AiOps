# Movie ticket pricing - 
# prices based on age: $12 for adults(18 and over), $8 for children. 
# Everyone gets a $2 discount on wednesday 


age = int(input("Enter you age: "))
day = input("enter the day: ")

price = 12 if age >= 18 else 8
if day == "Wednesday":
    price = price-2

print(f"Ticket price for you on {day} is $",price)