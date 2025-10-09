Why use tuple if list exists?
Tuples are faster, memory efficient, and hashable, so they can be used as dictionary keys or in sets.

Q2: Can a tuple contain mutable objects?
Yes. Tuple khud immutable hai, but uske andar list, dict jaise mutable objects ho sakte hain.

Q3: What happens if you try to modify a tuple element?
You’ll get TypeError: 'tuple' object does not support item assignment.

Q4: Can you sort a tuple?
Why tuple.sort() doesn’t work & what does tuple(sorted(t)) mean?
Tuples immutable hote hain → isliye unke paas .sort() method nahi hota.
Sorting ke liye elements ko rearrange karna padta hai, jo immutability ke against hai.
No, tuples don’t have .sort() method. But you can do:

sorted(t)

sorted() ek built-in Python function hai jo kisi bhi iterable (list, tuple, string) ko sorted list me convert kar deta hai.

It doesn’t modify the original tuple — it just returns a new list with sorted elements.

print(sorted(t))   # [1, 2, 5, 9]

sorted_tuple = tuple(sorted(t))