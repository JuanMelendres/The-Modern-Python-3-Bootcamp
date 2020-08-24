# ask for age
age = input("How old are you: ")

#if age:
#   if int(age) >= 18 and int(age) < 21:
        # 18-21 wristband
#        print("You can enter, but need a wristband!")
#    elif int(age) >= 21:
        # 21+ drink, normal entry
#        print("You are good to enter and can drink!")
#    else:
        # too young, sorry
#        print("Yoy can´t come in, little one! :(")
#else:
#    print("Please enter an age!")

if age:
    age = int(age)
    if age >= 21:
        print("You are good to enter and can drink!")
    elif age >= 18:
        print("You can enter, but need a wristband!")
    else:
        print("Yoy can´t come in, little one! :(")
else:
    print("Please enter an age!")