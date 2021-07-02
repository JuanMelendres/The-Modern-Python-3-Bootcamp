# Tuple an ordered collection or grouping of items (immutable)
numbers = (1, 2, 3, 4)

print(3 in numbers)
# numbers[0] = "Change me" # TypeError: 'tuple' object does not support item assignment

# Tuples can be used ad keys in dictionaries:
locations = {
    (35.6895, 39.6917): "Tokyo Office",
    (50.7128, 74.0060): "New York Office",
}

# ------------- Looping & Methods ------------- #
numbers = (1, 2, 3, 4, 4, 4)
for num in numbers:
    print(num)

# Count returns the number of times a value appers in a tuple

print(numbers.count(1))
print(numbers.count(4))

# Index returns the index at which a value is found in a tuple
print(numbers.index(1))
print(numbers.index(3))
