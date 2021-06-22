numbers = [1, 2, 3, 4]
# For loop
for number in numbers:
    # print(number)
    print(number * number)

print("")

# While loop
i = 0
while i < len(numbers):
    print(f"{i}: {numbers[i]}")
    i += 1

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

result = ""
for sound in sounds:
    result += sound.upper()

print(result)