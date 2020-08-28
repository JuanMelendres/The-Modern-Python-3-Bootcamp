'''
# While loop
i = 1
while i < 11:
    print("\U0001f600" * i)
    i += 1
'''

'''
# For loop
for num in range(1, 11):
    print("\U0001f600" * i)
'''

# Whitout string multiplication (ugly solution)
for num in range(1, 11):
    count = 1
    smileys = ""
    while count < num:
        smileys += "\U0001f600"
        count += 1
    print(smileys)

print("")

# While 2 times
i = 1
while i < 20:
    print("\U0001f600" * i)
    i += 2