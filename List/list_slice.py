# First paramether where to start
first_list = [1, 2, 3, 4, 5, 6]
print(first_list[1:])
print(first_list[3:])
print(first_list[-1:])

# Second paramether where to end
first_list = [1, 2, 3, 4, 5, 6]
print(first_list[:3])
print(first_list[1:3])

# Thirtd paramether is step -> step is basically the number to count at a time
first_list = [1, 2, 3, 4, 5, 6]
print(first_list[1::2])
print(first_list[::2])

#tricks with Slice

# Reversing list / strings
string = "This is fun!"
print(string[::-1])

palindrome = "salas"
if palindrome == palindrome[::-1]:
    print(f"Palindrome: {palindrome}")

# Modifying portions of list
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = ['a', 'b', 'c']
print(numbers)

# Swapping Values
names = ["James", "Michelle"]
print(names)
names[0], names[1] = names[1], names[0]
print(names)