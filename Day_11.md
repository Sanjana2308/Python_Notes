# Python
## Class
### Class name should always start with a capital letter
```python
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
### Printing objects of a class and its datatype
```python
# print(ferrari["name"]) # ❌ error
print(type(ferrari), type("cool"))  # <class '__main__.Car'> <class 'str'>
print(ferrari.name, ferrari.wheels)
```

### Instance Method and Instance Variable
Instance Method:  An instance method in object-oriented programming is a function or procedure that operates on an instance of a class. It's associated with objects instantiated from the class and typically acts upon the data contained within those objects.<br>

Instance Variable: An instance variable, also known as a member variable, is a variable defined in a class for which each instantiated object of the class has its own separate copy. <br>
```python
class Car:
    def __init__(self, name, engine, wheels, doors): 
        # Instance Variables
        self.name = name
        self.engine = engine
        self.wheels = wheels
        self.doors = doors

    # Instance method
    def horn(self):
        return f"{self.name} says Vroom Vroom"
    
ferrari = Car("Ferrari", "v8", 4, 2)
alto = Car("Alto", "v4", 4, 4)
print(ferrari.name, ferrari.wheels)
print(ferrari.horn()) # Ferrari says Vroom Vroom
print(alto.horn()) # Alto says Vroom Vroom
```
### Writing Numbers:
We can write numbers as:
![alt text](Numbers.png)
### Tasks
#### Task 1:
Create a class Bank with following Instance Variables
```
Schema:
Bank Account
1. acc_no
2. name
3. balance
```
```
Data:
Amisha - 50_000
Mathesh - 70_000
Sai Ganesh - 65_000
```
```python
class Bank:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

amisha = Bank(121, "Amisha", 50_000)
mathesh = Bank(122, "Mathesh", 70_000)
sai_ganesh = Bank(123, "Sai Ganesh", 65_000)
```

#### Task 2: 
Display balance for each customer.
```python
class Bank:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def display_balance(self):
        print(f"{self.name} your bank balance is ₹{self.balance}")

amisha = Bank(121, "Amisha", 50_000)
mathesh = Bank(122, "Mathesh", 70_000)
sai_ganesh = Bank(123, "Sai Ganesh", 65_000)

print(amisha.name)
amisha.display_balance()
mathesh.display_balance()
sai_ganesh.display_balance()
```

#### Task 3:
Create a function withdraw.
```python
class Bank:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def display_balance(self):
        return f"{self.name} your bank balance is ₹{self.balance}"

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Insufficient funds. {self.display_balance()}"

amisha = Bank(121, "Amisha", 50_000)
mathesh = Bank(122, "Mathesh", 70_000)
sai_ganesh = Bank(123, "Sai Ganesh", 65_000)

print(mathesh.display_balance())
print(mathesh.withdraw(10_000))
print(mathesh.display_balance())
print(mathesh.withdraw(90_000))
```

#### Task 4:
Create a function deposit.
```python
class Bank:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def display_balance(self):
        return f"{self.name} your bank balance is ₹{self.balance}"

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Insufficient funds. {self.display_balance()}"

    def deposit(self, amount_d):
        if amount_d >= 0:
            self.balance = self.balance + amount_d
            return f"Amount Updated. {self.display_balance()}"
        else:
            return f"Insufficient Amount. {self.display_balance()}"

amisha = Bank(121, "Amisha", 50_000)
mathesh = Bank(122, "Mathesh", 70_000)
sai_ganesh = Bank(123, "Sai Ganesh", 65_000)

print(mathesh.deposit(10_000))
``` 

### Encapsulation 
Properties + action(logic)
It refers to the bundling of data (attributes) and methods (functions or procedures) that operate on that data into a single unit, called a class. The main idea behind encapsulation is to hide the internal state and behavior of an object from the outside world and only expose a limited interface through which the object can be interacted with.

### Class Variable
```python
class Bank:
    # Class Variable: All your instances share the class variable
    interest_rate = 0.02

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def display_balance(self):
        return f"{self.name} your bank balance is ₹{self.balance}"

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Insufficient funds. {self.display_balance()}"

    def deposit(self, amount_d):
        if amount_d >= 0:
            self.balance = self.balance + amount_d
            return f"Amount Updated. {self.display_balance()}"
        else:
            return f"Insufficient Amount. {self.display_balance()}"

    def apply_interest(self):
        self.balance = self.balance + self.balance*self.interest_rate
        return f"Interest received. {self.balance * self.interest_rate}"

tonika = Bank(126, "Tonika", 1_50_000)
manasa = Bank(127, "Manasa", 80_000)

print(Bank.interest_rate)

# After one year
print(tonika.apply_interest())
print(manasa.apply_interest())

print(tonika.display_balance())
print(manasa.display_balance())
```

### Static Method - @staticmethod
A static method in Python is a method that belongs to a class but does not operate on the instance of the class (i.e., it doesn't access or modify instance attributes). It is defined using the @staticmethod decorator. Static methods can be called on the class itself or on instances of the class.

### Class Method - @classmethod
A class method in Python is a method that operates on the class itself rather than on instances of the class. It is defined using the @classmethod decorator and takes a special first argument conventionally named cls, which represents the class itself. Class methods can access and modify class-level variables but not instance variables.

### Normal function
A normal function in Python is defined using the def keyword. 

### Super charge to the normal method
It refers to enhancing the functionality or performance of a normal method by using techniques like optimization, parallelization, or other advanced programming practices. Essentially, it means making a normal method more powerful or efficient.

In Python, you can sometimes enhance the functionality of a normal method by using certain decorators, like @staticmethod or @classmethod, to change its behavior or the way it interacts with the class or its instances. This could be seen as "supercharging" the method, although it's not a widely-used term in this context.


```python
# pi is a global variable
pi = 3.14
def perimeter(radius):
    return 2*pi*radius
```

### Implementation of static method and class method
```python
class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def perimeter(radius):
        return 2*Circle.pi*radius
    
    def cal_area(self):
        return Circle.pi*self.radius**2
    
    @classmethod
    def diameter(cls, diameter):
        # To construct the object
        radius = diameter/2
        print(cls.pi)
        return cls(radius)

# Normal function but inside class - no access to self
print(Circle.perimeter(5))

# Instance method
c1 = Circle(4)
print(c1.cal_area())

# Class method - to cinstruct the object
c_from_diameter = Circle.diameter(10)
print(c_from_diameter.cal_area())
```
1. Static Method (perimeter): it doesn't require access to the instance (self) or the class (cls) and can be called directly on the class. It uses the class variable pi.
2. Instance Method (cal_area): This method calculates the area of the circle. It uses the instance variable radius (accessible through self) and the class variable pi to compute the area.
3. Class Method (diameter): This method is used to construct a Circle object given its diameter. It takes the diameter as an argument, calculates the radius, and then constructs a Circle object using that radius. It's decorated with @classmethod, so it takes cls (the class itself) as its first argument and has access to class variables like pi.
4. Circle.perimeter(5): Calls the static method perimeter directly on the Circle class to calculate the perimeter of a circle with radius 5.
5. c1 = Circle(4): Creates an instance of the Circle class with a radius of 4.
6. c1.cal_area(): Calls the instance method cal_area() on the c1 object to calculate the area of the circle with radius.
7. Circle.diameter(10): Calls the class method diameter directly on the Circle class to construct a Circle object with a diameter of 10. It prints the value of pi and returns the constructed Circle object.
8. c_from_diameter.cal_area(): Calculates the area of the circle constructed with a diameter of 10 using the diameter class method.


### Tasks for @classmethod and @classmethod :
#### Task 1 :
Add 2 functions<br>
Bank.get_total_no_of_accounts() and <br> 
Bank.update_interest_rate(0.10)
<br> to the class Bank

```python
class Bank:
    # Class Variable: All your instances share the class variable
    interest_rate = 0.02
    no_of_accounts = 0

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        Bank.no_of_accounts += 1

    def display_balance(self):
        return f"{self.name} your bank balance is ₹{self.balance}"

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Insufficient funds. {self.display_balance()}"

    def deposit(self, amount_d):
        if amount_d >= 0:
            self.balance = self.balance + amount_d
            return f"Amount Updated. {self.display_balance()}"
        else:
            return f"Insufficient Amount. {self.display_balance()}"

    def apply_interest(self):
        self.balance = self.balance + self.balance*self.interest_rate
        return f"Interest received. {self.balance * self.interest_rate}"

    # If we would have used a normal method outside the class we would have got the same result but because of encapsulation we are keeping all the methods together inside the class
    # static method is used when we want to display a value which should not change for different instances of the class
    @staticmethod
    def get_total_no_of_accounts():
        return f"In total there are {Bank.no_of_accounts} accounts"
    
    # Here we need to do the modification to the class i.e. we need to get the access of the class thus using @classmethod
    @classmethod
    def update_interest_rate(cls, interest):
        cls.interest_rate = interest


sneha = Bank(128, "Sneha", 1_00_000)
siva = Bank(129, "Siva", 90_000)

print(Bank.get_total_no_of_accounts())
Bank.update_interest_rate(0.10)

print(sneha.apply_interest())
print(sneha.display_balance())
```

### Access Specifiers
1. private - __balance (double underscore)
2. protected - _balance (single underscore)
3. public - balance (no underscore)

```python
class Bank:
    # Class Variable: All your instances share the class variable
    interest_rate = 0.02
    no_of_accounts = 0

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        Bank.no_of_accounts += 1

    def display_balance(self):
        return f"{self.name} your bank balance is ₹{self.balance}"

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Insufficient funds. {self.display_balance()}"

    def deposit(self, amount_d):
        if amount_d >= 0:
            self.balance = self.balance + amount_d
            return f"Amount Updated. {self.display_balance()}"
        else:
            return f"Insufficient Amount. {self.display_balance()}"

    def apply_interest(self):
        self.balance = self.balance + self.balance*self.interest_rate
        return f"Interest received. {self.balance * self.interest_rate}"

    # If we would have used a normal method outside the class we would have got the same result but because of encapsulation we are keeping all the methods together inside the class
    # static method is used when we want to display a value which should not change for different instances of the class
    @staticmethod
    def get_total_no_of_accounts():
        return f"In total there are {Bank.no_of_accounts} accounts"
    
    # Here we need to do the modification to the class i.e. we need to get the access of the class thus using @classmethod
    @classmethod
    def update_interest_rate(cls, interest):
        cls.interest_rate = interest


divya = Bank(128, "Divya", 1_00_000)
priya = Bank(129, "Priya", 90_000)

# This 👇 should be not allowed 
divya.balance = -80000 
print(divya.balance)
```
We need to change balance to a private variable so that it is not accessible.

```python
# We need to change the balance variable to private to get rid of the above error
def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = __balance
        Bank.no_of_accounts += 1
```
```python
# Error:
print(divya.balance) # internal usage
```

```python
class Bank:
    # Class variable | All your instance share the class variable
    __interest_rate = 0.02
    __no_of_accounts = 0

    def __init__(self, acc_no, name, balance):
        # instance variable
        self.__acc_no = acc_no
        self.__name = name
        self.__balance = balance
        Bank.__no_of_accounts += 1

    @staticmethod
    def get_total_no_accounts():
        return f"In total we have {Bank.__no_of_accounts} accounts"

    @classmethod
    def update_interest_rate(cls, new_interest_rate):
        cls.__interest_rate = new_interest_rate

    def display_balance(self):
        return f"Your balance is: ₹{self.__balance:,}"

    def withdraw(self, amount):
        if self.__balance - amount >= 0:
            self.__balance -= amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Insufficient funds. {self.display_balance()}"

    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Invalid amount. {self.display_balance()}"

    def apply_interest(self):
        accumulated_interest_amt = self.__balance * Bank.__interest_rate
        self.__balance += accumulated_interest_amt
        return f"Interest received. ₹{accumulated_interest_amt}"


divya = Bank(130, "Divya", 1_00_000)
priya = Bank(131, "Priya", 90_000)

print(divya.apply_interest())
print(divya.display_balance())
# Interest received. ₹2000.0
# Your balance is: ₹102,000.0
```

# Convention
1. Privatize all the instance and class variables.
2. Access to instance and class variables done through public methods 

## Inheritence
1. Parent class: Animal
```python
class Animal:
    def __init__(self, name):
        self.name = name

    # methods/attributes
    def speak(self):
        return "Some sound"

toby = Animal("toby")
print(toby.speak())
```
2. Child class: Dog
```python
class Animal:
    def __init__(self, name):
        self.name = name

    # methods/attributes
    def speak(self):
        return "Some sound"
    
class Dog(Animal):
    def run(self):
        return "🐶 wags tail!!"
    
maxy = Dog("maxy", 20)
print(maxy.run())
# speak() inherited from parent class Animal
print(maxy.speak())
```
3. Overriding Methods
```python
class Animal:
    def __init__(self, name):
        self.name = name

    # methods/attributes
    def speak(self):
        return "Some sound"
    
class Dog(Animal):
    def run(self):
        return "🐶 wags tail!!"
    def speak(self):
        return "Woof!!🐶"
    
maxy = Dog("maxy")
print(maxy.run())
# speak() is overriden here - Polymorphism i.e. we can morph according to the class
print(maxy.speak())
```
4. super keyword
```python
class Dog(Animal):
    # Initiate the base class constructor using super
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

    def run(self):
        return "🐶 wags tail!!"

    def speak(self):
        return "Woof!!🐶"
    
maxy = Dog("maxy", 20)
print(maxy.name)
print(maxy.run())
print(maxy.speak())
```
5. We can override the method if we want to
<br>and<br>
whenever we have extra variables in the child class we need to initiate the constructor.

```python
class Animal:
    def __init__(self, _name):
        self._name = _name

    # methods/attributes
    def speak(self):
        return "Some sound"
    
class Dog(Animal):
    # Initiate the base class constructor using super
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

    def run(self):
        return "🐶 wags tail!!"

    def speak(self):
        return "Woof!!🐶"
    
    def speed_bonus(self):
        return f"{self._name} running at {self.speed*2}Km/hr"
    
maxy = Dog("maxy", 20)
print(maxy._name)
print(maxy.run())
print(maxy.speak())
print(maxy.speed_bonus())
```
Set the attributes to protected if it is inherited otherwise keep it private.

#### Task 5:
SavingsAccount - Interest_Rate -->0.05<br>
sabesh = SavingsAccount(131, "Sabesh", 80_000)<br>
print(sabesh.get_balance())<br>
```python

```

#### Task 6:
withdraw transaction_fee - 10 rupees<br>
class CurrentAccount:<br>
    pass<br>
tanishq = SavingsAccount(131, "Tanishq", 80_000)<br>
print(tanishq.withdraw(1_000))<br>
print(tanishq.withdraw(10_000))<br>
print(tanishq.get_balance())<br>
```python

```








