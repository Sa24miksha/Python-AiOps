# check is the password is "Weak","Medium" or "Strong"
# criteria- less than 6 - weak 
# 6-10 char - medium 
# >10 -  strong 

passowrd = input("Enter you password: ")
length = len(passowrd)

if length < 6:
    print("Password is weak")
elif length <10:
    print("Password is medium")
else:
    print("Password is strong")

