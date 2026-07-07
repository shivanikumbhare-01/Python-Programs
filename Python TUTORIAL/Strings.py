# strings in python
# strings - chars in single,double and triple quotes
name='shivani'  #creating a string
print(name)

print(type(name))  #checking datatype
print("It's name")
print('''"My name is shivani"''')

# Formatted strings
# 1.Old style fomratting - %operator
name='Shivani'
age=21
print("My name is %s and I'm %d" %(name,age))
# %s and %d are placeholders for the strings and integer

# 2. str.format() method
name='Shivani'
age=21
print("My name is {} and I'm {}".format(name,age))

# you can reference variables by index or keyword
print("My name is {0} and I'm {1}".format(name,age))
print("My name is {1} and I'm {0}".format(name,age))

print("My name is {name} and I'm {age}".format(name='Savita',age=40))

# 3. f-strings
name='Shivani'
age=21
print(f"My name is {name} and I'm {age}")
print(f"My  age after 2 years will be {age+2}")


# strinng operators in python
a='Hello'
b='Python'
print(a+b)  #concatenate
print(a*2)  #multiple copies

if'H'  in a:
    print('Yes')
else:
    print('No')

print('Hello\nWorld')

# STring indexing
my_name='Shivani'
# index=0123456
print(my_name[0])   #first character of string
print(my_name[1])   #second character of string
print(my_name[2])   #third character of string
print(my_name[3])   #fourth character of string
print(my_name[4])   #fifth character of string
print(my_name[5])   #sixth character of string

# String slicing
# syntax: string[start:end:step]

name='shivani' 
#index:0123456
print(name[0:4:3])
print(name[0:5:2])
print(name[0:4:1])
print(name[1:4:3])

print(name[2:5])
print(name[-1:])
print(name[6])
print(name[-2:])
print(name[::])


# string methods
word='Hello, shivani'

# 1.len()
print(len(word))

# 2.upper()
print(word.upper())

# 3.lower
print(word.lower())

# 4.count()
print(word.count('i'))

# 5.find()
print(word.find('h'))

# 6.split()
print(word.split(','))
print(word.split( ))

# 7.Replace()
print(word.replace('shivani','Savita'))

# 8.Title()
print(word.title( ))

# 9.strip()
word2='  Hello World  '
print(len(word2))
print(word2.strip())

# 10.join()
zword=('Shivani', 'is', 'Great')
print(' '.join(zword))
print('-'.join(zword))




























