# A normal function
def add(a, b):
    return a+b
print(add(3, 8))

# Lambda function
add1 = lambda a, b: a+b
print(add1(3, 11))

add2 = lambda x: x+100
print(add2(50))

# Immediately Invoked Function Expression
print((lambda a, b: a*b)(15, 2))

# We can use keyword arguments in Lambda Function
product = lambda a, b, c: a*b*c
# It is not necessary to write the value of variables in a specific order in funtions in Python
print(product(c = 5, a = 10, b = 4))

# Using default arguments
add3 = lambda x, y = 15, z = 24: x+y+z
print(add3(20))
# Passed only one argument because y and z are set as default

# Use * - Pass as many arguments as u want
addition = lambda *args: sum(args)
print(addition(20, 40, 2, 50))

# Used with higher order functions which  take one or more functions as argument or return one or more functions
higher_ord_fun = lambda x, fun: x + fun(x)
print(higher_ord_fun(20, lambda x : x*x))

# odd or even
print((lambda x: (x % 2 and 'odd' or 'even'))(30))

# To check if a string is a substring of a given string
sub_string = lambda string: string in "Welcome to Python Functions Tutorial"
print(sub_string("Python"))

# Use a list of numbers using filter()
num = [10, 40, 56, 27, 33, 15, 70]
greater = list(filter(lambda num: num > 30, num))
print(greater)

# filter()
list1 = [10, 40, 56, 27, 33, 15, 70]
divide = list(filter(lambda x: (x%4 == 0), list1))
print(divide)

# Use Map function with lambda function
list2 = [10, 40, 56, 27, 33, 15, 70]
double_the_num = list(map(lambda x: x*2, list2))
print(double_the_num)

# Power of a number raised to 3
list3 = [2, 5, 10, 6, 4, 12]
cube = list(map(lambda x: x**3, list3))
print(cube)

# How to use reduce() inside lambda() and lambda() inside User defined functions
# Use reduce() - Find the sum of all the values present in the list
# Importing reduce()
from functools import reduce
list4 = [2, 5, 10, 6, 4, 12]
sum = reduce((lambda x, y: x+y), list4)
print(sum)

# Using lambda function inside a user defined function
def quadratic(a, b, c):
    return lambda x: a*x**2 + b*x + c
f = quadratic( 2, 3, 5)
print(f(1))
# Where x = 1, a = 2, b = 3, c = 5