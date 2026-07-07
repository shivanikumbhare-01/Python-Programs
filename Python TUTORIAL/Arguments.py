# Arguments in python

# 1. Required Arguments (Single/multiple arguments)
def greetings(name):   #name is parameter 
    print("Hello",name,"!")
greetings('Shivani')  # shivani is argument

def intro(course_name,instructor_name):
    print("Welcome to ", course_name,"course by",instructor_name)
intro("Python","Shivani")

# 2.Default arguments
def greetings(name="World"):   #"world is a default value"
    print("Hello",name,"!")

greetings()   #runs without error using default value
greetings('shivani')

# 3.Keyword arguments
def divide(a,b):   #"world is a default value"
    return a/b
result1=divide(100,20)  #positional argument
print(result1)

result2=divide(a=100,b=20)  
print(result2)

result3=divide(b=100,a=20) #keyword argument
print(result3)

#4.Arbitary Argument
# Arbitary Positional Argument(*args)
# stores arguments as tuple
def add2number(a,b):
    return a+b
result=add2number(9,1)
print(result)

def add3number(a,b,c):
    return a+b+c
result1=add3number(9,1,1)
print(result1)

def add_numbers(*args):
    return sum(args)

op=add_numbers(5,2,1,5)  #variable no. of arguments
print(op)

def function(*names):
    for name in names:
        print(f"Hello,{name}!")
function('shivani','kumbhare')

# Arbitary Keyword Argument(*kwargs)
# value is in dictionary format here
def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_details(name='shivani',age=21,city='Nagpur')