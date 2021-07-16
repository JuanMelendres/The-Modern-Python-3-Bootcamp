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

print(multiple_letter_count("awesome"))
