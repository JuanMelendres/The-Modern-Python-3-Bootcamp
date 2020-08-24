# And operator
age = 6 

if age > 2 and age < 8:
    print("YOU PAY CHILD PRICE!")

# Or operator

city = input("Where do you live? ")

if city == "los angeles" or city == "san francisco":
    print("YOU LIVE IN CALIFORNIA!")
else:
    print("YOU LIVE SOMEWHERE ELSE")

ages = 21
# 2-8 2 dollar ticket
# 65 5 dollar ticket
# 10 dollars for everyone else

if not ((ages >= 2 and ages <= 8) or ages >= 65):
    print("YOU PAY 10 DOLLARS AND ARE NOT A CHILD O SENIOR!")
else:
    print("YOU ARE A CHILD OR SENIOR!")