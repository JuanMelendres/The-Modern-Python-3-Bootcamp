# Variables and Conventions in Python 3

###Variables

**Assign a variable:**
    
```python
num_of_cats = 99
print(num_of_cats)
```

**Reassign a variable:**
    
```python
num_of_cats = num_of_cats - 1
print(num_of_cats)

num_of_cats = num_of_cats * 2
print(num_of_cats)

num_of_pets = num_of_cats
print(num_of_pets)
```

**Assign multiple variables:**
```python
five, six, seven = 5, 6, 7
```

###Conventions

**Varibles should be snake_case and lowercase:**
```python
num_of_cats = 10
```

**Only constants are uppercase:**
```python
PI = 3.14
```

UpperCalmelCase is for a class and Variables that start and wend with two underscores are supposed to be private or left alone.

**Dinamic typing:**
```python
awesomeness = True
print(awesomeness)

awesomeness = "a dog"
print(awesomeness)

awesomeness = None
print(awesomeness)

awesomeness = 22 / 7
print(awesomeness)
```