# Assignment -5 on Loops

# 1. print in the same line
print('Hello',end=' ')
print('Madhav')

# by using while loop 
i=1
while i<4:
    print(f'Hello Madhav{i}', end=' ')
    i+=1

# 2.print star patterns - using loop
# nested loop to print  triangle pattern
n=5  #number of rows
for i in range(1,n+1):  #outer loop no. of rows
    for j in range(1,i+1):   #inner loop for columns(1 to 5)
        print('*',end=' ')   #print star without new line
    print()         #move to the next line after each row/iteration

# by using easy method
for i in range(1,n+1):
    print('*'*i)

# inverted triangle 
# nested loop to print inverted triangle pattern
n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()

# by using easy method
for i in range(n,0,-1):
    print('*'*i)

# pyramid pattern
n=5 
for  i in range(1,n+1):  #loop for  no. of rows
    print(' ' * (n-i),end=' ')  #spaces to center the stars
    print('*' *(2*i-1))  #print stars


# 3.factorial of number

def factorial(n):
    result=1
    while n>0:
        result*=n
        n-=1
    return result
print(factorial(4))

# 4.count vowels in a string
my_string='Python by Shivani '
vowels='aeiou'
count=0

for char in my_string:
    if char.lower() in vowels:
        count+=1
print('Number of vowels are',count)

# 5.Longest word in a string
sentence='Python by shivani'
words=sentence.split()
longest_word=''

for word in words:
    if len(word)>len(longest_word):
        longest_word=word
print('The longest word is:',longest_word)


# 6. do-while loop in python
while True:
    num=int(input('Enter a number greater than 10:'))
    if num>10:
        print(f'valid number entered:{num}')
        break  #exit the loop when the condition is satisfied
    else:
        print('Number is not greater than 10,try again!')

# 7:Fibonacci Sequence

def fibonacci(n):
    a,b=0,1
    count=0
    while count<n:
        print(a)
        a,b=b,a+b
        count +=1
fibonacci(10)





















