# Assignment2
#Write a program to input student name  & marks of 3 subjects.
#Print name and percentage in output


# student_name=input("Enter your name:")
# hindi_marks=input("Enter your hindi marks:")
# maths_marks=input("Enter your maths marks:")
# Science_marks=input("Enter your Science marks:")

# #calculating percentage
# percentage=((int(hindi_marks)+int(maths_marks)+int(Science_marks))/300)*100


# #print resullt
# print(f"The result of {student_name} is {int(percentage)}%. Well done!")

#Q2: Write a Python program that collects multiple types of data (e.g., name, age, height, and student status) from user input, stores them in a dictionary, and then prints out the collected data.

#initializing a dictionary
user_data={}

#input from user
user_data['name']=input("Enter your name:")
user_data['age']=input("Enter your age:")
user_data['height']=float(input("Enter your height:"))
user_data['student']=input("are you a student(yes/no):")

#print the input from user
print(user_data)











