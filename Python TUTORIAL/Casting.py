#Casting in python
#It means chyanging datatype


a=1
print(type(a))

b="1"
print(type(b))

c=int(b)
print(type(c))

print(a+c)

#all str type can't be casted into numerical ttype
#all numeric type can be cast into str
mynum=21
mynum2=str(mynum)
print(type(mynum2))

f1=21.33
f2=int(f1)
print(f2)
print(type(f2))

int =24
print(type(float(int)))


#implicit type casting 
var1=10  #int type
var2=12.4
var3=var1+var2
print(var3)
print(type(var3))

#Explicit type casting
int_num=102
str_num=str(int_num)
print(type(str_num))

a0=bool(0)
print(a0)
print(type(a0))

a0=bool(1)
print(a0)
print(type(a0))
