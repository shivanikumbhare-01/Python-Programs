#Loops in python- Nested loop-Loop inside another loop

# syntax

# outer loop:
#     inner loop:
        # block of code for inner loop
# block of code for outer loop

# print numbers from 1 to 3 for 3 times
# using for loop
for i in range(3):
    for num in range(1,4):
        print(num)
    print('-------')

# by using while loop:nested loop
i=1
while i<4:
    for j in range(1,4):
        print(j)
    print('-----')
    i+=1

# print prime numbers between range of 2 to 10  using nested  loop

for  num in range(2,20):
    for i in range(2,num):
        if num % i==0:
            break
        else:
            print(num)













