# functions in python

# create function without parameter
def grettings():
    print('Welcome to the python course by Shivani!')
# call function (use function)
grettings()

# create a function to add 2 numbers using parameter
def addnumbers(num1,num2):   #parameters:(num1,num2)
    addition=num1+num2
    print('Addition of num1+num2is:',addition)
# call above function
addnumbers(5,3)  #arguments(5,3)
addnumbers(num1=2,num2=4)

# create a function to add 3 numbers
def addnumbers(num1,num2,num3):   #parameters:(num1,num2)
    addition=num1+num2+num3
    print('Addition of num1+num2+num3 is:',addition)
# call above function
addnumbers(5,3,2)  #arguments(5,3,2)

# function with return statement
def addnum(a,b):
    return a+b 
    # return a+b after return statement function end ,if u write any line after that it doesn't make any sense
sum_num=addnum(10,1)
print(sum_num)

# functions to convert celsius to Farenheit-return statement
def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
# call function
temp_f=celsius_to_fahrenheit(25)
print(temp_f)

# functions to convert celsius to Farenheit-without return statement
def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    print(fahrenheit)
# call function
celsius_to_fahrenheit(50)                                                                   









