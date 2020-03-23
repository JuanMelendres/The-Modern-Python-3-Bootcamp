'''
Set the variable called first to your first name.
Set the variable called last to your last.
Then set the variable called formatted that interpolates both using the .format() method. 
Make sure you follow this pattern: "First Name: Colt, Last Name: Steele"
'''

first = "Juan"
last = "Melendres"
# .format method:
formatted = "First Name: {}, Last Name: {}".format(first, last)
# F-String method:
#formatted = f"First Name: {first}, Last Name: {last}")"

print(formatted)