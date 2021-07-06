# list Comprehension
def generate_evens():
    return [num for num in range(1,50) if num % 2 == 0]

#Lopping
def generate_evens():
    result = []
    for x in range(1,50):
        if x % 2 == 0:
            result.append(x)
    return result