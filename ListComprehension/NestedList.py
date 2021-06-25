nested_list = [[1,2,3], [5,4,6], [7,8,9]]

# print(nested_list[0][2])
# print(nested_list[1][2])
# print(nested_list[2][2])

# Nested List looping 

for i in nested_list:
    for j in i:
        print(j)

# Nested List Comprehension

[[print(j) for j in i] for i in nested_list]

board = [[num for num in range(1,4)] for val in range(1, 4)]
print(board)

print([["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)])

# ------------- Problem 5 Solution ------------- #

board = [[num for num in range(0,3)] for val in range(0, 3)]
print(board)

# ------------- Problem 6 Solution ------------- #

board = [[num for num in range(0,10)] for val in range(0, 10)]
print(board)