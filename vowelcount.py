string = "What a wonderful day to program."
tot = 0
for char in string:
    if char in ['a','e','i','o','u']:
        tot+=1
print(tot)
