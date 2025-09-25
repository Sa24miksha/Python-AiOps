student = {
    "name": "Samiksha", 
    "age": 22, 
    "course": "CSE"
    }

print(student["name"])    # Samiksha

# Adding/updating
student["age"] = 23
student["branch"] = "AI"
print(student)

# Methods
print(student.keys())     # dict_keys(['name','age','course','branch'])
print(student.values())   # dict_values(['Samiksha',23,'CSE','AI'])
print(student.items())    # dict_items([('name','Samiksha'),...])
