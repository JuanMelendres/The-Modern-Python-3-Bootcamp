def exponent(num, power=2):
    return num ** power

print(exponent(2,3))
print(exponent(3,3))
print(exponent(7))

print("")

def add(a=10, b=20):
    return a + b

print(add())
print(add(25+25))

print("")

def show_information(first_name="Colt", is_instructor=False):
    if first_name == "Colt" and is_instructor:
        return "Welcome back instructor Colt!"
    elif first_name == "Colt":
        return "I really thought you were an instructor..."
    return f"Hello {first_name} !"

print(show_information())
print(show_information(is_instructor=True))
print(show_information('Molly'))

print("")

def add(a, b):
    return a + b

def math(a, b, fn=add):
    return fn(a, b)

def substract(a, b):
    return a - b

print(math(2, 2))

print(math(2, 2, substract))

print("")

# Exercise
def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"

print(speak())

def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"

# Keyword Arguments only works if we know the name of the parameters

def full_name(first, last):
    """Documenting Functions"""
    return f"your name is {first} {last}"

print(full_name(first='Juan', last='Melendres'))
print(full_name(last='Melendres', first='Juan'))