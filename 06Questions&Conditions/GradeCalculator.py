# Assign a letter grade basend on the studnets 
# score : A (90-100), B(80-89), C(70,79), D(60-69), F(Below 60)


Marks = int(input("Enter your marks: "))

if Marks >= 101:
    print("Please verify you grade marks again")
    exit()

if Marks >= 90:
    grade = "A"
elif Marks >= 90:
    grade = "B"
elif Marks >= 70:
    grade = "C"
elif Marks >= 60:
    grade = "D"
else:
    grade = "F"     

print("Marks obtained: " , grade)   