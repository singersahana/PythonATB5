# Write a program to take the input from the user
# and Sum those two numbers
# Mul --> *
# div --->/

# Logic building
# step1
# Input --> num1,num2 ---> int
# Output ---> sum--->int,sub--->int,div--->float
# num1 = input("Enter the num1\n")
# num2 = input("Enter the num2\n")
# If we are not using int means it will take only string
# str --> int

num1 = int(input("Enter the num1\n"))
num2 = int(input("Enter the num2\n"))
print(type(num1))
print(type(num2))

# step2 | rough logic
# sum -->+,-,/,*

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
# step3
print("sum is :",sum)
print("sub is:",sub)
print("mul is:",mul)
print("div is:",div)