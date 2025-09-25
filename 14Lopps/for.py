#  for loop → iterate over sequence

fruits = ["apple","banana","mango"]
for fruit in fruits:
    print(fruit)


#  Range - 
for i in range(5):  # 0,1,2,3,4
    print(i)


# while loop → repeat while condition is True
print("While looop: ")


i = 0

while i <= 5:
    print(i)
    i += 1

# Loop control: break, continue, pass
print("Continue, Break & Pass: ")
for i in range(5):
    if i == 3:
        break       # exit loop
    if i == 1:
        continue    # skip current iteration
    print(i)


# for → iterating over list, dict, or range → best for known number of repetitions


