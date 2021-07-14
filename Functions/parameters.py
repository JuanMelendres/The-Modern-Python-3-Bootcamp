def square(num):
    return num**2

result = square(9)
print(result)
print(square(4))

def sing_happy_birthday(name):
    print("Happy Birthday To You")
    print("Happy Birthday To You")
    print(f"Happy Birthday Dear {name}")
    print("Happy Birthday To You")

sing_happy_birthday('Juan')

def multiply(first, second):
    return first * second

print(multiply(5, 2))

def print_full_name(first_name, last_name):
    return (f"Your full name is {first_name} {last_name}")

print(print_full_name('Juan', 'Melendres'))

# Exercise
def yell(word):
    return(word.upper()+"!")

print(yell('go away'))

def yell(word):
    return "{}!".format(word.upper())

def yell(word):
    return f"{word.upper()}!"