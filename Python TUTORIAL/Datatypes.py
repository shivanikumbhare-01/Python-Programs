#data types in python
a=1
b=2
print(a+b)
print(type (a+b)) #checking data type:integer

c="1"
d="1"
print(c+d)
print(type(c))  #checking data type:string

#basic data types in python:
#1. Numeric
a=1  #1a.integer
b=1.5 #1b.float
print(type(b))
c=complex(3,5) #1c.Complex
print(type(c))


#2.Sequence
b1="Shivani"  #2a.string
print(type(b1))
b2=[1,2,3,"shiv"] #2b.List
print(type(b2))
b3=(1,2,3,"Shiv") #2c.Tuple
print(type(b3))

#3.Dictionary
my_dictionary={'name':'Rishabh','age':26,'city':'Nagpur'}
print(type(my_dictionary))

#4.Sets
my_sets={1,2,3,'Shiv'}
print(type(my_sets))

#5.Boolean
bool1=True
bool2=False
print(type(bool1))

#6.Binary
#bytes,bytearray,memoryview
byte1=b'shiv'
print(type(byte1))