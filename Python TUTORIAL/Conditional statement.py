# conditional statement in python
# 1.if statement
# If statement works only for true condition
a=25
b=190
if b>a:
    print("b is  greater than a")

age=26
if age>19:
    print('you are an adult')

age=int(input('Enter your age:'))
if age>19:
    print('you are an adult')

# If-else statement
# else handle false condition
age=int(input('enter your age:'))
if(age>19):
    print('You are an adult')
else:
    print('YOu are not an adult')

temp=30
if temp<24:
    print('its a cool day')
else:
    print('its a hot day')

# 3.if-elif-else statement
# multiple conditions

marks=int(input('Enter your marks-100:'))
if marks>=90:
    print('Grade: A+')
elif marks>=80:
    print('Grade A')
elif marks>=70:
    print('Grade b') 
elif marks>=60:
    print('Grade C') 

# 4.Nested if -else statement:  
# if-else inside if-else statement 
# multiple conditions depend on each other  

# Q. Positive,negative and zero positive-even/odd
num=int(input('Enter a number:'))  
if num>0: #checking positive number 
    if num%2==0:
        print('This is a even number')
    else:
        print('This is an odd number')   
else:
    if num==0: 
        print('This is zero')
    else:
        print('This is a negative num')    


# Conditional expressions (Ternary operator)
 
marks=40
Result="Pass" if marks>=40 else"Fail"
print(Result)

# Assignment -3
# Leap year program
# user input
year=int(input("Enter a year"))

# # checking leap year
if  (year%4==0 and year%100 !=0) or(year%400==0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")

# Que.2.Login Authentication using conditional statement

# predefined username and password
predefined_username='shivani'
predefined_password='pass123'

username=input('Enter you username')
password=input('Enter your password')

if username==predefined_username:
    if password==predefined_password:
        print('Welcome! Login was successful.')
    else:
        print('Incorrect password')
else:
    print('Invalid Username')








