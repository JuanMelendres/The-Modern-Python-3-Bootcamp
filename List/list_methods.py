demo_list = [1, 2, 3, 4]
print(demo_list)

# ------------------- Insert ------------------- #

# Append add to the end of the list (only one value).
demo_list.append(5)
print(demo_list)

demo_list.append("Hi")
print(demo_list)

# Extend add to the end of the list all values passed (multiple value).
demo_list.extend(["Orange", 6, 7])
print(demo_list)

# Insert an item at a given position
demo_list.insert(0, "The beginning")
print(demo_list)

demo_list.insert(len(demo_list), "The end")
print(demo_list)

# ------------------- Delete ------------------- #

# Clear remove all items from the list
demo_list.clear()
print(demo_list)

# Pop remove the items at the given position, if no index specified removes the last item and return the item.
demo_list = [1, 2, 3, 4]
demo_list.pop(0)
print(demo_list)

demo_list.pop()
print(demo_list)

# Remove the first item from the list whose value is X, throw ValueError if the item is not found.
demo_list = [1, 2, 3, 4]
demo_list.remove(3)
print(demo_list)

# ------------------- Index ------------------- #

# Index return the index of the specified item in the list
demo_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(demo_list.index(5))
print(demo_list.index(5, 1))

# ------------------- Count ------------------- #

# Count return the number of times x appears in the list
demo_list = [1, 2, 3, 4, 5, 6, 7, 8, 5, 5, 7, 8]
print(demo_list.count(5))

# ------------------- Reverse ------------------- #

# Reverse the elements of the list (in-place)
demo_list = [1, 2, 3, 4, 5, 6, 7, 8, 5, 5, 7, 8]
print(demo_list)
demo_list.reverse()
print(demo_list)

# ------------------- Sort ------------------- #

# Sort the items of the list (in-place, ascending order)
demo_list = [1, 2, 3, 4, 5, 6, 7, 8, 5, 5, 7, 8]
demo_list.sort()
print(demo_list)

# ------------------- Join ------------------- #

# Join converts the list into a string
demo_list = ["Hello", "world", "!!"]
print(' '.join(demo_list))

# ------------------- Exercise ------------------- #

# Create a list called instructors
instructors = []

# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.extend(["Colt", "Blue", "Lisa"])

# Remove the last value in the list
instructors.pop()

# Remove the first value in the list
instructors.pop(0)

# Add the string "Done" to the beginning of the list
instructors.insert(0, 'Done')