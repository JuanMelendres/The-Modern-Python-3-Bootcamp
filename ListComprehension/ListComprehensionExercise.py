# ------------- Problem 1 Solution ------------- #

answer = [friend[0] for friend in ["Elie", "Tim", "Matt"]]

answer2 = [num for num in [1, 2, 3, 4, 5, 6, 7, 8] if num % 2 == 0]

# ------------- Problem 2 Solution ------------- #

answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]

answer2 = [friend[::-1].lower() for friend in ["Elie", "Tim", "Matt"]]

# ------------- Problem 3 Solution ------------- #

answer = [num for num in range(1,101) if num % 12 == 0]

# ------------- Problem 4 Solution ------------- #

answer = [char for char in "amazing" if char not in "aeiou"]
print(answer)