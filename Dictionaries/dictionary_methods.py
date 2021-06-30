# ---------- Clear ---------- #

# Clears all the keys and values in a dictionary

d = dict(a=1, b=2, c=3)
print(d)
d.clear()
print(d)

# ---------- Copy ---------- #

# Makes a copy of a dictionary

d = dict(a=1, b=2, c=3)
c = d.copy()
print(d)
print(c)

# ---------- Fromkeys ---------- #

# Crates key-value pairs form comma separated values: 

print({}.fromkeys("a", "b"))
print({}.fromkeys(["email"], "unknown"))
new_user = {}.fromkeys(["email", "name", "score"], "unknown")
print(new_user)

# ---------- Get ---------- #

# Retrieves a key in an object and return None
# Instead of a key error if the key does not exist.

d = dict(a=1, b=2, c=3)
print(d['a'])
print(d.get('a'))
print(d.get('d'))

# ---------- Pop ---------- #

# Takes a single argument corresponging to a key and removes that key-value pair from the dictionary.
# Returns the value corresponding to the key that was removed.

d = dict(a=1, b=2, c=3)
print(d)
d.pop('a')
print(d)

# ---------- PopItems ---------- #

# Removes a random key in a dictionary

d = dict(a=1, b=2, c=3)
print(d)
d.popitem()
print(d)

# ---------- Update ---------- #

# Update keys and values in a dictionary with another set of key value pairs.

d = dict(a=1, b=2, c=3, d=4, e=5)
a = {}
a.update(d)
print(a)