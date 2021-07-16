'''
product(2,2) # 4
product(2,-2) # -4
'''
# define product below:
def product(a, b):
    return a * b

# print(product(2, -2))

'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''
    
def return_day(num):
    days = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
    day = days.get(num)
    if day:
        return day
    return None

# print(return_day(12))

# Others solutions

def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None

def return_day(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None

'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(list):
    if list:
        return list[-1]
    return None

# print(last_element([]))

'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

def number_compare(a, b):
    if a > b:
       return "First is greater"
    elif a < b:
        return "Second is greater"
    return "Numbers are equal"

# print(number_compare(1, 2))

'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

#define single_letter_count below:
def single_letter_count(str, letter):
    return str.lower().count(letter.lower())

# print(single_letter_count("Hello World", "h"))

'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# flesh out multiple_letter count:
def multiple_letter_count(str):
    return {char: str.count(char) for char in str}

# print(multiple_letter_count("awesome"))

'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(list, command, location, value=None):
    if value:
        if location == "end":
            list.append(value)
            return list
        else:
            list.insert(0, value)
            return list
    else:
        if location == "end":
            return list.pop()
        else:
            return list.pop(0)

# print(list_manipulation([1,2,3], "add", "beginning", 20))

# Another Solution

def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection

'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''

def is_palindrome(str):
    return str == str[::-1]

# Another Solution

def is_palindrome(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]

# print(is_palindrome('testing'))

'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

def frequency(list, search_term):
    return list.count(search_term)

# print([1,2,3,4,4,4], 4)

'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(lst):
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total

# print(multiply_even_numbers([2,3,4,5,6]))

'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize(str):
    return str[:1].upper() + str[1:]

# print(capitalize("tim"))

'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact(lst):
    return [value for value in lst if value]

#  Another solution
def compact(l):
    truthy_vals = []
    for val in l:
        if val: truthy_vals.append(val)
    return truthy_vals

# print(compact([0,1,2,"",[], False, {}, None, "All done"]))

# flesh out intersection pleaseeeee
def intersection(a, b):
    return [val for val in a if val in b]

# Another Solutions
def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]

def intersection(l1, l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common

# print(intersection([1,2,3], [2,3,4]))

'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''

def isEven(num):
    return num % 2 == 0

def partition(list, fn=isEven):
    truthy_list = []
    falsy_list = []
    for num in list:
        if fn(num):
            truthy_list.append(num)
        else:
            falsy_list.append(num)
    return [truthy_list, falsy_list]

# Another Solutions 
def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]

def partition(l, callback):
    return [[l.pop(l.index(i)) for i in l if callback(i)],l]

# print(partition([1,2,3,4], isEven))