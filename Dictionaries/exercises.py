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
# answer = dict.fromkeys()
[[print(i, j) for j in i] for i in person]