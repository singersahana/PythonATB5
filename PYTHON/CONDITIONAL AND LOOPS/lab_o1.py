# Write a program to take a user input
# let him, know that he can go to club or not
# age = 21
# --------------------------------------------------------------------------------
# step1:
# i/p -->age --> datatype  ---> int
# o/p -->string -->he can go or not
# --------------------------------------------------------------------------------
# step2:
# rough logic [brute force logic]
# age>21 --> he can go to the club
# age<21 ---> he can't go to the club
# --------------------------------------------------------------------------------
# step3:
# logic
age = int(input("enter the age\n"))
if age >=21:
    print("He go to the club\n")
else:
    print("He can't go to the club\n")
# --------------------------------------------------------------------------------
# step4:check for the edge cases
# we should consider the edge cases such as:
# negative ages  and extremely high values --> then program will break
# Non numeric input -ABC
# Age is valid only >130
# --------------------------------------------------------------------------------
# step5: optimization
# handle the all edge cases