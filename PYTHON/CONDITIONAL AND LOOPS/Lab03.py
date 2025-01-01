#Problem to find the max b/w two no
#

#  Logic Building formula

# step 1:
# i/p --> two integers
# o/p --> one int
# 31.5 or 45.34 --> float
# ------------------------
num1 = float(input("Enter the first no\n"))
num2 = float(input("Enter the Second no\n"))

if num1>=num2:
    print("Maximum is ", num1)
else:
    print("Maximum is ", num2)
# ------------------------
# edge cases
# num1==num2 ---> handled
# string --> ABC, ten --> error
# we can handle this using try and catch block
