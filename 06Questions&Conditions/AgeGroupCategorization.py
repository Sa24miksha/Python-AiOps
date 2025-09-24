# Classify the person's age group : Child(< 13),Teenagers(13-19), Adult(20-59),Seniorz(60+)

age = int(input("enter your age: "))
if age < 13:
    print("You're a child")
elif age < 20:
    print("Teenager!")
elif age <60:
    print("Adult!")
else:
    print("Senior")