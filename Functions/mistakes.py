def sum_odd_number(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
        # return total # is wrong
    return total

print(sum_odd_number([1,2,3,4,5,6,7,8]))

def is_ood_number(num):
    if num % 2 != 0:
        return True
    return False

print(is_ood_number(2))