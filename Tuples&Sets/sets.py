# Sets formal mathematical sets

# Creating a new set

s = set({1,2,3})
s = {1,2,3}

# ------------- Looping & Methods ------------- #
for a in s:
    print(a)

# Add adds an element to a set.

s.add(4)
print(s)

# Removes removes an element to a set.

s.remove(4)
print(s)

s.discard(3)
print(s)

# Copy copy the set.

another_s = s.copy()
print(another_s)

# clear clear the set.

another_s.clear()
print(another_s)

# Union
a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 4, 5, 6, 7, 8}

print(a | b)

# Intersections
a = {1, 2, 3, 4, 5}
b = {1, 5, 6, 7, 2}

print(a & b)