nums = [1, 2, 3, 4]

# List Comprehension
print([x*10 for x in nums])

# -------------- List Comprehension vs Looping -------------- #

# Lopping

numbers = [1, 2, 3, 4, 5]
double_numbers = []

for num in numbers:
    double_number = num * 2
    double_numbers.append(double_number)

print(double_numbers)

# List Comprehension

numbers = [1, 2, 3, 4, 5]
double_numbers = [num * 2 for num in numbers]
print(double_numbers)

name = ["juan"]
print([char.upper() for char in name])

friends = ['karen', 'luis', 'misael', 'jose']
print([friend[0].upper() for friend in friends])

print([num * 10 for num in range(1,6)])

print([bool(val) for val in [0, [], '']])

numbers = [1, 2, 3, 4, 5]
string_list = [str(num) for num in numbers]
print(string_list)