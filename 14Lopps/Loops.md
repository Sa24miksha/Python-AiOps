Difference between range and for loop

range() → generates a sequence of numbers on the fly.

for loop → iterates over a sequence (like list, tuple, string, or the range object).

Example:

for i in range(5):    # range generates 0,1,2,3,4
    print(i)


Here range(5) → sequence [0,1,2,3,4]

for i in range(5) → iterates over that sequence

Key: range() just gives numbers, for loop actually does the repeating work

You can also iterate over list directly without range:

fruits = ["apple","banana","mango"]
for f in fruits:
    print(f)


💡 Memory note:

range() generates numbers lazily → doesn’t store huge list in memory

This is efficient for large loops