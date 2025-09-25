# Ordered and mutable 

fruits = ["apple", "banana", "orange"]

print(fruits[0])

fruits.append("kiwi") 
print(fruits)

fruits.insert(1,"papaya")
print(fruits)

fruits.remove("banana")
print(fruits)

print(fruits.pop())
print(fruits)

print(len(fruits))
print("apple" in fruits)


# Important list methods -
nums = [1,2,5,3,8,5,2,7,0,8,4,6,7]

nums.reverse()
print(nums)

nums.sort()
print(nums)

print(nums.count(2))

print(nums.index(1))

nums.clear()
print(nums)

nums.copy()
print(nums)


# nexted list
list1 = [1,2,3,4,5,6,9,10]
list1.append([7,8])
print(list1)

# merged list
list2 = [1,2,3,4,5,6,9,10]
list2.extend([7,8])
print(list2)


# various operatiosn on list 

li = [1,2,3,4,5,6,9,10]
print(sum(li))


# popping element 
li.pop()
print(li)


# min and max
print(max(li))
print(min(li))



# Problem: What if you want the index of 2nd occurrence?

# Python doesn’t have built-in method for that, you can do:

# li = [1,2,3,2,3,2]
# first = li.index(2)
# second = li.index(2, first + 1)
# print(second)   # 3

# list.index(value, start_index) → searches from start_index onwards.

