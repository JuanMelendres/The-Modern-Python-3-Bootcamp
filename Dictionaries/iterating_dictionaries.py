instructor = {
    "name": "Colt",
    "owns_dog": True,
    "nums_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "My favorite number!"
}

# print(instructor["name"])
# print(instructor["owns_dog"])
# print(instructor["nums_courses"])
# print(instructor["favorite_language"])
# print(instructor["is_hilarious"])
# print(instructor[44])

# Accessing All values in a dictionary

for value in instructor.values():
    print(value)

# Accessing All keys in a dictionary

for value in instructor.keys():
    print(value)

# Accessing All keys and values in a dictionary

for value in instructor.items():
    print(value)

for keys, value in instructor.items():
    print(f"key is {keys} and value is {value}")

# ------------- Problem 2 Solution ------------- #

# DON'T TOUCH PLEASE!
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# DON'T TOUCH PLEASE!

# Use a loop to add together all the donations and store the resulting number in a variable called total_donations
total_donations = 0
for v in donations.values():
    total_donations += v

print(total_donations)

# Advanced version 1
total_donations = sum(donation for donation in donations.values())
print(total_donations)

# Advanced version 2
total_donations = sum(donations.values())
print(total_donations)

# Does a dictionary have a key?
print("name" in instructor)
print("phone" in instructor)

# Does a dictionary have a value?
print("Colt" in instructor.values())
print("Nope!" in instructor.values())
