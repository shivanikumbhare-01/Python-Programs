# user inout
print('Enter PCM marks out of 100')
physics_marks=int(input('Enter physics marks:'))
Chemistry_marks=int(input('Enter Chemistry marks:'))
Maths_marks=int(input('Enter Maths marks:'))

# Eligibility checks
if (Maths_marks>=65 and
  physics_marks>=55 and
  Chemistry_marks>=50 and
  (Chemistry_marks+Maths_marks+physics_marks)>=180) or \
  (Maths_marks+physics_marks)>=140:
    print("you're eligible")
else:
    print("you're not eligible") 














