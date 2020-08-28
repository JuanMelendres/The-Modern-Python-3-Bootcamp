for i in range(1, 21):
    if i == 4 or i == 13:
        state = ("UNLUCKY")
    elif i % 2 != 0:
        state = ("odd")
    else:
        state = ("even")
    print(f"{i} is {state}")
