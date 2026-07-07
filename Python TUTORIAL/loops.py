# Loops in python - while & for loop

# WHILE LOOP  - as long as condition is true
count=0
while count<5:  #condition
    print(count)
    count=count+1

# print numbers from 1 to 5 using while loop
count=1
while count<6:  #condition
    print(count)
    count=count+1

count=5
while count>0:  #condition
    print(count)
    count=count-1
else:
    print('while loop ended')

# check conditions to avoid infinte loop

# for loop - iterates over sequence
language='Python'  #sequence
for x in language:
    print(x)

# range function
# range(stop)
# range(start,stop,step)
for i in range(5):  #stop argument
    print(i)

for i in range(5,10):  #start , st0p argument
    print(i)

for i in range(5,10,2):    #start , stop,step argument
    print(i)

for i in range(5):
    print(i)
else:
    print('for loop ended')

# LOOP CONTROL STATEMENTS
# 1.Pass statement

for i in range(5):
    pass

count=5
while count>0:
    if count==3:
        pass
    else:
        print(count)
    count-=1
print('---------')
# 2.Break statement
for i in range(6):
    if i ==4:
        break
    print(i)

print('----------')
# 3. Continue statemet

for i in range(6):
    if i ==4:
        continue
    print(i)























