# Example 1
name = "Sanjana"
job = "engineer"

if job == "army":
    print(name+" is an army officer")
elif job == "engineer":
    print(name+" is an engineer")
else:
    print(name+" does some other job")

# Example 2
name1 = "Sanjana"
job1 = "engineer"
age1 = 22

if job == "army":
    print(name+" is an army officer")
elif job == "engineer":
    if age1 > 30:
        print(name+" is an old "+job)
    else:
        print(name+" is a young "+job)    
else:
    print(name+" does some other job")

# Example 3
opp = "div"
num1 = 10
num2 = 20

if opp == "add":
    print(num1 + num2)
elif opp == "sub":
    print(num1 - num2)
elif opp == "mul":
    print(num1 * num2)
elif opp == "div":
    print(num1 / num2)
else:
    print("Wrong Operation")