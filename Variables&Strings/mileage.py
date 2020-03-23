print("How many kilometers didi you cycle today?")
kms = input()
#print("ok, you said " + kms)
miles = float(kms) / 1.60934
miles = round(miles, 2)
#round(thing to round, how many decimal points)
print(f"Your {kms} km ride was {miles} mi")
