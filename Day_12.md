# Python

## Error Handling Tasks:

## break and continue
break - Used to stop a loop
continue - skip one iteration
return - exits out of function

1. break Example
```python
for num in range(1, 10):
    if num==5:
        break
    print(num)
```
```python
def print_nums():
    for num in range(1, 10):
        if num == 6:
            break

        print(num)
    print("Execution continues 🎊")
print_nums()
```

2. continue Example
```python
def skip_even():
    for num in range(1, 10):
        if num % 2 == 0:
            continue
        print(num)
    print("Execution continues 🎊")
skip_even()
```

### Tasks for break and continue
Task 1: Find the first negative value 
```
Test case:
print(first_negative([3, 5, 7, -1, 9, -3]))  # -1
```
```python
def first_negative(numbers):
    neg = None
    for num in numbers:
        if num < 0:
            neg = num
            break
    return neg
print(first_negative([3, 5, 7, -1, 9, -3]))  # -1
```

Task 2: Print until you find a duplicate value
```
process_until_duplicate(["apple", "banana", "carrot", "apple", "date", "banana"])

Expected output
Processed apple
Processed banana
Processed carrot
Duplicate found, processing stopped.
```

```python
def process_until_duplicate(fruits):
    fruit_set = set()
    for fruit in fruits:
        if fruit in fruit_set:
            print("Duplicate found, processing stopped.")
            break
        fruit_set.add(fruit)
        print(f"Processed {fruit}")
    print(f"Operation Done")

process_until_duplicate(["apple", "banana", "carrot", "apple", "date", "banana"])
```

Task 3:
```
messages = [
    "Hello everyone!",
    "This is a bad word example!",
    "Let's keep our chat clean!",
    "Oops another bad content!",
    "Have a nice day!",
]

banned_words = ["bad", "oops"]

Expected output
Approved message: Hello everyone!
Approved message: Let's keep our chat clean!
Approved message: Have a nice day!
```
Use nested loops
```python
Day_13
```

## Multi Line String
```python
print("""
This is cool
We will do it
This is cool
      """)
```

```python
followers = 10_000
name = "Manju"
print(
    f"""
Hi this is {name},
I have {followers} followers
"""
)
```
Documentation
```python
# """ """ or ''' '''
# Documentation
def to_upper_case(text):
    # The documentation to be given should be the first line of the function
    """
    This helps in converting the text into uppercase
    """
    return text.upper() + " 🎊"


print(to_upper_case(name))
print(help(to_upper_case))
```