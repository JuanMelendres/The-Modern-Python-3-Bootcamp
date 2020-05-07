# Variables and Conventions in Python 3

## Variables

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

## Conventions

**Variables should be snake_case and lowercase:**

```python
num_of_cats = 10
```

**Only constants are uppercase:**

```python
PI = 3.14
```

UpperCalmelCase is for a class and Variables that start and wend with two underscores are supposed to be private or left alone.

**Dynamic typing:**

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

## Strings

**F-Strings:**

```python
x = 10
formated = f"I´ve told you {x} times already!"
```

**.formated method:**

```python
x = 10
formated = f"I´ve told you {} times already!".format(10)

fruit = "banana"
ripeness = "unripe"
print("The {} is {}".format(fruit, ripeness))
```

**% operator (deprecated):**

```python
x = 10
formated = "I´ve told you times already!" % (x)
```

## Data types

**Integer:**

```python
decimal = 12.56345634534
integer = int(decimal) #12
```

**String:**

```python
my_list = [1, 2, 3]
my_list_as_a_string = str(mylist) #"[1, 2, 3]"
```

**Float:**

```python
num = 12
num = float(num) #12.0
```
