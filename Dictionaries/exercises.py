# ------------- dictionary Exercises ------------- #

# ------------- Problem 1 Solution ------------- #

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]: list2[i] for i in range(0,3)}
print(answer)

#  Advanced solution
answer = dict(zip(list1,list2))
print(answer)

# ------------- Problem 2 Solution ------------- #

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {thing[0]: thing[1] for thing in person} # {k:v for k,v in person} or dict(person)
print(answer)

# ------------- Problem 3 Solution ------------- #

vowels = [["a", 0], ["e", 0], ["i", 0], ["o", 0], ["u", 0]]
# make sure your solution is assigned to the answer variable so the tests can work!
answer = dict(vowels)
print(answer)

# Others solutions 
answer = {char:0 for char in 'aeiou'}
answer = dict.fromkeys("aeiou", 0)