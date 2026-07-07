# Assignment 4

# 1.Limit the decimal places to 2 digits using dot(.) format method and print result, for the variable pi=3.14159265359

pi=3.14159265359

print('Value of pi is {}'.format(pi))

# Using f function formatting float number
print('The value of pi is {:.2f}'.format(pi))  #when you want only two  values after point
print('The value of pi is {:.1f}'.format(pi))  #when you want only one  values after point
print('{:.2f}'.format(pi))   #another method ...it also gives same output
# 
# f-strings
print(f'{pi:.2f} using f-string')

# Que.2. Extract characters  from index 2 to 8 with a step of 2: Given my_string ='Python Course',slice characters from index 2 to 8 ,skipping every other char.
my_string ='Python Course'
print(my_string[2:8:2])

# Que.3.Slice to get only the middle character(s): For my_string ='Shivani', use slicing to extract the middle character(s).
my_string ='Shivani'  #7 chars-odd
 
my_string2='Madhav'  #6 chars-even

def mid_str(word):
    middle=int(len(word)/2)
    if len(word) % 2==0:
        return word[middle-1:middle+1]
    else:
        return word[middle]
print(mid_str(my_string))
print(mid_str(my_string2))

# Que.4. Remove the first 3 characters: Given my_string='Regression Analysis',remove the first 3 and last 3 characters.
my_string='Regression Analysis'
print(my_string[3:-3])

# /Que5.Get the substring that starts 4 characters from the end to the last character: For my_string ='Classification',slice the string starting from the 4th character from the end to the last character.
my_string ='Classification'
print(my_string[-4:])

# Que.6.How to Reverse a string using python string methods?
word='shivani'
print(word[::-1])  #step value=-1

# que.7.Write a python function to check if a string is a palindrome using string methods.
word='madam'
name='shivani'

def is_palindrome(s):
    if s==s[::-1]:
        print(f'{s} is a palindrome')
    else:
        print(f'{s} is not a palindrome')

is_palindrome(word)  #here we calling a function
is_palindrome(name)
















