# Python
## Cheatsheet of Iterable and Sequence from Bookmarks Chrome

### PEP - Python Enhancement Proposals
1. All the arguments should be in proper indentation

2. For method_names write lower_case_with_underscore

3. For constant names write UPPER_CASE_WITH_UNDERSCORE

PEP states the rules to write code in a proper format.
1. For Commenting we can use String Documentation
```python
"""
Documentation
String
of
Multiline
"""
```

### Set Comprehension

```python
colors = ["red", "blue", "red", "green", "pink", "blue"]
unique_colors = set()
for color in colors:
    unique_colors.add(color)
print(unique_colors)

# Set Comprehension
unique_colors_1 = {clr for clr in colors}
print(unique_colors_1)
```

#### Task:
Find the length of words
```python
words = ["This", "is", "cool", "mangoes", "oranges", "apples"]
#{4, 2, 7, 5}
words_length = {len(word) for word in words}
print(words_length)
```

### Dictionary Comprehension
```python
squares = {x: x**2 for x in range(1, 11)}
print(squares)
```

### Nested Loops
```python
classes = {
    "Class A": [
        {"name": "Alice", "grades": [82, 90, 88]},
        {"name": "Bob", "grades": [78, 81, 86]},
        {"name": "Charlie", "grades": [85, 85, 87]},
        {"name": "Alex", "grades": [85, 90, 87]},
    ],
    "Class B": [
        {"name": "Dave", "grades": [92, 93, 88]},
        {"name": "Eve", "grades": [76, 88, 91]},
        {"name": "Frank", "grades": [88, 90, 92]},
    ],
}
```

#### Task 1:
Find the average of whole class
```python
def find_avg(items):
    return round(sum(items)/len(items), 2)

class_avg = {}
for class_name, students in classes.items():
    class_student_avg = []
    for student in students:
        avg = find_avg(student["grades"])
        class_student_avg.append(avg)
    class_avg[class_name] = find_avg(class_student_avg)
print(class_avg)

# output = {
# "Class A" : 82.53 ,
# "Class B" : 85.50 
# }
```

1.2 With List Comprehension
```python
class_avg = {}
for class_name, students in classes.items():
    class_students_avg = [find_avg(student["grades"]) for student in students]
    class_avg[class_name] = find_avg(class_students_avg)
print(class_avg)
# output = {
# "Class A" : 82.53 ,
# "Class B" : 85.50 
# }
```
1.3. List comprehension for both for loops
```python
class_avg = {class_name: find_avg([find_avg(student["grades"]) for student in students])
            for class_name, students in classes.items() 
            }
print(class_avg)
# output = {
# "Class A" : 82.53 ,
# "Class B" : 85.50 
# }
```

#### Task 2:
Find the average of each student.
2.1: Without List Comprehension
```python
class_wise_student_avg = {}
for class_name, students in classes.items():
    class_student_avg = {}
    for student in students:
        avg = find_avg(student["grades"])
        print(student["name"], avg)
        class_student_avg[student["name"]] = avg
    class_wise_student_avg[class_name] = class_student_avg
print(class_wise_student_avg)    
# output = {
#     "Class A": {"Alice": 90.50, "Bob": 84.50, "Charlie": 90.00},
#     "Class B": {"Dave": 92.50, "Eve": 86.50, "Frank": 950},
# }
```

2.2: With List Comprehension
```python


# output = {
#     "Class A": {"Alice": 90.50, "Bob": 84.50, "Charlie": 90.00},
#     "Class B": {"Dave": 92.50, "Eve": 86.50, "Frank": 950},
# }
```

## All Vs Any
All -  works like 'and' logical operator
And - works like 'or' logical operator
```python
print(all([True, False, True])) # False
print(any([True, False, True])) # True
```

### Task:
Whether person gets a grade or not - 40/ more is the pass percentage.<br>
Output:<br>
No, they will not get a grade<br>
Yes, they will get a grade<br>
```python
marks = [50, 40, 20, 90]
if all(mark > 40 for mark in marks):
    print("Yes, they will get a grade")
else:
    print("No, they will not get a grade")
```



