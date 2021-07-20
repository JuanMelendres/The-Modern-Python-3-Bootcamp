def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all_nums(4,6,9))

def ensure_correct_info(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"
    return "Not sure who you are..."

print(ensure_correct_info(1,True,"Steele","Colt"))

# Exercise

def contains_purple(*args):
    if "purple" in args:
        return True
    return False

print(contains_purple(1,True,"purple"))