# Write a generator function that yields even number up to a specified limit 

def even_generator(limit):
    for i in range(2, limit+1, 2):
        print(i)

even_generator(10)