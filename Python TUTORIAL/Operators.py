# operators
# 1.Arithmetic Operators
a=5
b=3
print(a+b)   
print(a-b)  
print(a*b)  
print(a%b) 
print(a/b)  


#2.Comparison Operators -output is boolean value(true/false)
a=5
b=3
print(a>b) #greater than operator 
print(a<b)  #less than operator 
print(a==b) # equal operator 
print(a!=b)  #not equal operator 

#3.Assignment operator 
a=5 #assignment operator 

# 4.logical operator-compare two values  
# Rule for  And operator  
# True+True=True 
# TRue+false=False  
# false+false=false     
a=10 
b=20  
print(a>10 & b<10)                                                                                                               
print(a==10 & b==20)

# Rule for Or operator
# True+True=True
# TRue+false=True
# false+false=false
print(a==10 or b<10)


# 'not' operator 
print(not(a==10 and b==20))

# 5.Identity operators - is, is not
x=[1,2,3]
y=x
z=[1,2,3]
print(x is y)  #is operator
print(x is z)  #on the basis of location it gives you result

print(x is not z)

# 6.Membership operator
my_list=['apple','orange','watermelon']
print('apple' in my_list)  #in operator
print('apple1' in my_list) 
print('apple2' not in my_list) #not in operator

# 7.Bitwise operators-AND,OR,XOR,NOR,etc
a=5      #5 in binary 0101
b=3      #3 in binary 0011
print(a&b)   #1 in binary 0001
  

  



