# Python

## get() and set() for a Dictionary
.get() = Returns the value of a dictionary entry<br>
.set() = Sets a value in the dictionary 

### Task for Dictionary
```python
employees = [
    {"name": "Sneha", "experience": 2},
    {"name": "Manju"},
    {"name": "Sai Subash", "experience": 4},
    {"name": "Manasa"},
]
```
#### Task 1: 
It has been a year hence update their experiences
```python
for employee in employees:
    employee["experience"] = employee.get("experience", 0) + 1
print(employees)
# Output:
# [
#     {"name": "Sneha", "experience": 3},
#     {"name": "Manju", "experience": 1},
#     {"name": "Sai Subash", "experience": 5},
#     {"name": "Manasa", "experience": 1},
# ]
```

#### Task 2:
Set a key status: (with values) Senior 5 or more, Mid-Level 3 to 5, Junior < 3
```python
for employee in employees:
    employee["experience"] = employee.get("experience", 0) + 1

    if employee["experience"] >= 5:
        employee["status"] = "Senior"
    elif employee["experience"] >=3 and employee["experience"] < 5:
        employee["status"] = "Mid-level"
    else:
        employee["status"] = "Junior"
print(employees)
# Output:
# [
#     {"name": "Sneha", "experience": 3, "status": "Mid-Level"},
#     {"name": "Manju", "experience": 1, "status": "Junior"},
#     {"name": "Sai Subash", "experience": 5, "status": "Senior"},
#     {"name": "Manasa", "experience": 1, "status": "Junior"},
# ]
```


### Multiple Variable Assignment
```python
a = 10
b = 10
c = 10
print(a, b, c)
```
```python
a = b = c = 10
print(a, b, c)
```

## Unpacking
Assign multiple values to multiple variables at once.
```python
poojitha, shivam, samar = ("Black current", "Choco chip", "Butterscotch") # Tuple
```
```python
poojitha, shivam, samar = "Black current", "Choco chip", "Butterscotch"  # Tuple
```
### Printing elements from variables to which the values actually belong
```python
print(poojitha) # Black current
print(shivam) # Choco chip
print(samar) # Butterscotch
```

### Assigning values to different variables collectively from a list
```python
movies = ["Mission Impossible", "JJK", "Avengers Infinity War"]
mathesh = movies[0]
nandini = movies[1]
devesh = movies[2]
print(mathesh)
print(nandini)
print(devesh)
```
OR
```python
movies = ["Mission Impossible", "JJK", "Avengers Infinity War"]
mathesh, nandini, devesh = movies
print(mathesh)
print(nandini)
print(devesh)
```

### Error:
Assigning values when there are less variables on the left hand side and more on the right side.
```python
t1, t2, t3 = [100, 200, 300, 400]
print(t1, t2, t3)
# Error: Too many values to unpack
```

### Solution 1 of the above error 
Use _ as a variable name but that value will be skipped while printing values.
```python
t1, t2, _, t3 = [100, 200, 300, 400]
print(t1, t2, t3)
# 100 200 400
```

### Solution 2 of the above error is Unpacking
Use * unpacking operator to assign rest of the values to the variable containing the unpacking operator.
```python
t1, t2, *t3 = [100, 200, 300, 400, 60, 40, 30]
print(t1, t2, t3)
# 100 200 [300, 400, 60, 40, 30]
```

### Task 1:
coordinates = [(5, 4), (1, 1), (6, 10), (9, 10)]<br>
For each point find the distance from origin<br>
1.1: Using for loop
```python
coordinates = [(5, 4), (1, 1), (6, 10), (9, 10)]
distance = []
for cord in coordinates:
    x = cord[0]
    y = cord[1]
    d = (x**2+y**2)**0.5
    distance.append(round(d, 2))
print(distance)
# [6.4, 1.41, 11.66, 13.45]
```
1.2: Use for loop + unpacking<br>
1.2.1:
```python
coordinates = [(5, 4), (1, 1), (6, 10), (9, 10)]
distance = []
for cord in coordinates:
    x, y = cord
    d = (x**2+y**2)**0.5
    distance.append(round(d, 2))
print(distance)
# [6.4, 1.41, 11.66, 13.45]
```
1.2.2:
```python
coordinates = [(5, 4), (1, 1), (6, 10), (9, 10)]
distance = []
for x, y in coordinates:
    d = (x**2+y**2)**0.5
    distance.append(round(d, 2))
print(distance)
# [6.4, 1.41, 11.66, 13.45]
```
1.3: Use unpacking + list comprehension
```python
coordinates = [(5, 4), (1, 1), (6, 10), (9, 10)]
distance = [round((x**2+y**2)**0.5, 2) for x, y in coordinates]
print(distance)
# [6.4, 1.41, 11.66, 13.45]
```

### Skipping multiple items from a list
```python
t1, t2, *_, t3 = [100, 200, 300, 400, 60, 40, 20]
print(t1, t2, t3)
# 100 200 20
```

### Copying one list to another using Unpacking operator (*)
```python
marks1 = [20, 50, 40, 60, 10, 20]
marks1_copy = [*marks1]
print(marks1, marks1_copy)
# [20, 50, 40, 60, 10, 20] [20, 50, 40, 60, 10, 20]
```

### Merging multiple lists
```python
l1 = [80, 50]
l2 = [40, 20]
total = [*l1, *l2] # l1 + l2
print(total)
# [80, 50, 40, 20]
``` 

### Using unpacking in a dictionary - **
#### Adding key-values in a dictionary
```python
movie = {
    "name": "John Wick",
    "year": 2014
}

mv1 = {**movie, "actor": "Keanu Reeves"}
print(mv1)
# {'name': 'John Wick', 'year': 2014, 'actor': 'Keanu Reeves'}
```

The key values if mentioned after copying of the dictionary again then they will be updated to a new value because we cannot have duplicate keys in a dictionary
```python
movie = {
    "name": "John Wick",
    "year": 2014
}

mv2 = {**movie, "actor": "Keanu Reeves", "year":2015}
print(mv2)
# {'name': 'John Wick', 'year': 2015, 'actor': 'Keanu Reeves'}
```

In the below example te year does not get updated because the value given afterwards is the value in movies i.e. 2014 and in a dictionary the value updated latest is the value which will be updated finally.
```python
movie = {
    "name": "John Wick",
    "year": 2014
}

mv3 = {"actor": "Keanu Reeves", "year":2015, **movie}
print(mv3)
# {'actor': 'Keanu Reeves', 'year': 2014, 'name': 'John Wick'}
```

## Functions
### Why do we need Functions?

```python
a = 8
b = 10
print("The sum is: ",a+b)

a1 = 80
b1 = 100
print("The sum is: ",a1+b1)

a2 = 800
b2 = 1000
print("The sum is: ",a2+b2)
```
In the above program we are writing the same piece of code again and again. Instead, we can make a function and use it in place of writing the same piece of code again and again.

1. Reuse: Functions allow the same piece of code to run multiple times.
2. Modularity: Break long programs up into smaller components.
3. Change in one place reflects everywhere.

### Components of a function
1. Declaration\Definition
2. Function name
3. Parameters
4. Function body

```python
# 1. Declaration\Definition - def add(a, b):
# 2. Function name - add
# 3. Parameter - a, b
# 4. Function body - return(a+b)
def add(a, b):
    return (a+b)
# Function call
print("The sum is: ",add(8, 10))# Arguments
print("The sum is: ",add(60, 70))
print("The sum is: ",add(600, 70))
print("The sum is: ",add(60.748494, 70.89898))
print("The sum is: ",add(160.748494, 170.89898))
```

#### Parameters Vs Arguments: 
Parameters: Parameters are the variables listed inside the parentheses in the function or method definition.<br>
Arguments: Arguments are the actual values that are passed to a function when it is called.

### Giving default values in a function
If we don't specify the default values then 
If we don't give a car name in the below example then Dezire will be taken as the car name by default.
```python
def driving_test(name, age, car = "Dezire"):
    if age >= 18:
        return f"{name} eligible for driving. You will be tested in {car}"
    else:
        return "Try again after few years 👶🍼"
    
print(driving_test("Sanjana", 22, "Creta"))

# Error 👇: If default argument was not given  
print(driving_test("Sai Subhash", 20))
```

### Types of Arguments
1. Postition Arguments - In the first call, age is passed first, which results in a positional argument error because the function expects name first.
```python
# First call : Gives error
print(driving_test(20, "Poojitha"))
```
2. Keyword Arguments - In the second call, keyword arguments are used to specify the parameter names explicitly.<br>
In the third call, all arguments are passed, but out of order. However, since keyword arguments are used, the function can correctly map them to the parameters.
```python
# Second call
print(driving_test(age=20, name="Poojitha"))
# Third call
print(driving_test("Abishek", car="Honda city", age=20))
```
Always write the positional arguments first and then the keyword arguments.

### Tasks for Function
```python
library_list = [
    {
        "title": "Python Programming",
        "author": "Eric Matthes",
        "year": 2019,
        "available": True,
    },
    {
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "year": 2020,
        "available": True,
    },
    {
        "title": "Learning Python I",
        "author": "Mark Lutz",
        "year": 2013,
        "available": False,
    },
    {
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "year": 2015,
        "available": True,
    },
    {
        "title": "Adavance Python",
        "author": "Mark Lutz",
        "year": 2015,
        "available": False,
    },
]
```
#### Task 1:
Add Book Function: Write a function add_book(library, new_book)
```python
def add_book(library, new_book):
    library.append(new_book)

book = {"title": "Fluent Python II", "author": "Alex", "year": 2016, "available": True}
add_book(library_list, book)
print(library_list)
```

#### Task 2:
Search Books by Author Function: Write a function search_by_author(library, author_name)
```python
# Using for loop
def search_by_author(library, author_name):
    author_books = []
    for book in library:
        if book["author"] == author_name:
            author_books.append(book)
    return author_books
print(search_by_author(library_list, "Mark Lutz"))
```

```python
# Using list comprehension - Pythonic way - code that is clear concise and efficient
def search_by_author(library, author_name):
    return [book for book in library if book["author"] == author_name]

print(search_by_author(library_list, "Mark Lutz"))
```

### Task 3:
Check Out Book Function: Write a function check_out_book(library, title) that marks a book as not available if it exists and is available in the library.
1. Book available
2. Book unavailable
3. Book doesn't exists
```python
# By using flag 
def check_out_book(library, title):
    flag_stock = False
    for book in library:
        if book["title"] == title and book["available"] == True:
            flag_stock = True
            book["available"] = False
            return f"Yes, {title} is available and successfully checked out ✅"
        elif book["title"] == title and book["available"] == False:
            flag_stock = True
            return f"No, {title} is unavailable ❌"
    if flag_stock == False:
        return f"{title} is not present in library ☠️"
```
### Performing multiple operations in a function
After return the function body completes, no other expressions will be implemented. So, in above task we don't need flag_stock.
```python
def add1(a, b):
    print("cool")
    return a + b

print(add1(5, 6))
# cool
# 11
```
```python
def check_out_book(library, title):
    for book in library:
        if book["title"] == title and book["available"] == True:
            book["available"] = False
            return f"Yes, {title} is available and successfully checked out ✅"
        elif book["title"] == title and book["available"] == False:
            return f"No, {title} is unavailable ❌"
    return f"{title} is not present in library ☠️"
```

#### .format() -> f""

### Inbuilt Functions
1. sum
```python
print(sum([5, 6, 7, 10])) #28
```

2. max
```python
print(max([5, 10, 7, 6])) # 10 - max from a list
print(max("abzcd")) # z - max from a string
print(max(6, 90, 8, 190, 8, 4)) # 190 - max from a tuple
```

3. min
```python
print(min([6, 10, 7, 5])) # 5 - min from a list
print(min("bzcd")) # b - min from a string
```

4. len
```python
print(len("Sanjana")) # 7 - For String 
print(len([20, 10, 30, 40])) # 4 - For list
print(len((20, 10, 30))) # 3 - For tuple
```

5. round
```python
print(round(160.748495454, 3)) # 160.748
```

### Importing inbuilt Functions
```python
from package_name import function_name
```

Import pprint function from pprint module
```python
import pprint from pprint
```

### Tasks
```python
movies = [
    {"title": "Inception", "ratings": [5, 4, 5, 4, 5]},
    {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4]},
    {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4]},
    {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5]},
    {"title": "Memento", "ratings": [4, 5, 4, 5, 4]},
]
```

#### Task 1:
Function add_avg_rating : Calculate the average of movie ratings
```python
from pprint import pprint 
def add_avg_ratings(movies):
    for movie in movies:
        movie['average_rating'] = sum(movie['ratings'])/len(movie['ratings'])
    return movies

pprint(add_avg_ratings(movies))
```

#### Task 2:
Break the above function into smaller functions
```python
def cal_avg_ratings(movie):
    return sum(movie["ratings"])/len(movie["ratings"])

def add_avg_ratings(movies):
    for movie in movies:
        movie["average_rating"] = cal_avg_ratings(movie)
    return movies

print(add_avg_ratings(movies))
```

### Arbitrary Arguments
Arbitrary arguments also known as *args allow a function to accept any number of positional arguments. This can be useful when you don't know how many arguments will be passed to the function or when you want to write a function that can accept a variable number of arguments. These arguments store values in the form of a tuple.
```python
def own_max(*nums):
    print(nums, type(nums))
    print(max(nums))
own_max(5, 6, 10)
own_max(5, 6, 10, 7, 80, 60)
# (5, 6, 10) <class 'tuple'>
# 10
# (5, 6, 10, 7, 80, 60) <class 'tuple'>
# 80
```

```python
def own_max(a, b, *nums):
    print(a, b, nums, type(nums))
    print(max(nums))

own_max(5, 6, 10)
own_max(5, 6, 10, 7, 80, 60)
# 5 6 (10,) <class 'tuple'>
# 10
# 5 6 (10, 7, 80, 60) <class 'tuple'>
# 80
```

1. Arbitrary Positional Arguments
```python
# *nums = *args - used to pass a variable number of arguments to a function 
def own_max(*nums):
    curr_max = nums[0]
    for n in nums: 
        if curr_max < n:
            curr_max = n
    return curr_max
print(own_max(5, 6, 10)) # 10
print(own_max(5, 6, 10, 7, 80, 60)) # 80
```

2. Arbitrary Keyword Arguments 
```python
# **people = **kwargs - allows to pass a variable - length argument dictionary with keywords to a function
def party(**people): # **people == p1, p2, p3
    print(people, type(people))
    print(people.values())
    return ",".join(people.values())
print(party(p1 = "Sanjana", p2 = "Khushi", p3 = "Drishti", p4 = "Prakrti"))
# {'p1': 'Sanjana', 'p2': 'Khushi', 'p3': 'Drishti', 'p4': 'Prakrti'} <class 'dict'>
# dict_values(['Sanjana', 'Khushi', 'Drishti', 'Prakrti'])
# Sanjana,Khushi,Drishti,Prakrti
```

### Lambda Functions
A lambda function in Python is a small anonymous function defined using the lambda keyword. It can have any number of arguments but can only have one expression. 
```
lambda arguments: expression
```
#### Normal Function
```python
def add(a, b):
    return round(a+b, 2)
```
#### Lambda Function
```python
add = lambda(a, b): a+b
```

## OOPS - Object Oriented Programming Language
Modeling our coding probems as real world objects.

Example
```
Car
What makes a car?
1. engine
2. wheels
3. name
4. doors
```

Car - 1
```
1. engine - v8
2. wheels - 4
3. name - Ferrari
4. doors - 2
```

Car - 2
```
1. engine - v4
2. wheels - 4
3. name - Alto
4. doors - 4
```

### Class
1. Car is a blueprint i.e. a Class in Python.<br>
Classes in Python contain attributes(data) and methods(functions)
```python
# Class Definition 
class Car:
    def __init__(self, name, engine, wheels, doors): # Creating an object calls __init__ (Construtor)
    # Attributes - name, engine, wheels, doors
        self.name = name
        self.engine = engine
        self.wheels = wheels
        self.doors = doors
# Object Creation
ferrari = Car("Ferrari", "v8", 4, 2)
alto = Car("Alto", "v4", 4, 4)
# Printing Objects
print(ferrari.name, ferrari.wheels)
```





