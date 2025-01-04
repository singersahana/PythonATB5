#create a program to sum of three numbers from the user input,
# if user doesn't enter any numbers use 100,200,300
from PYTHON.FUNCTIONS.Functions_types import result

num1 = int(input("enter the num1\n"))
num2 = int(input("enter the num2\n"))
num3 = int(input("enter the num3\n"))

def sum_of_three_num(n1=100,n2=200,n3=300):
    return n1+n2+n3

result = sum_of_three_num(num1,num2,num3)
print(result)
# if didn't pass any arguments it will default arguments
result1=sum_of_three_num()
print(result1)

# -----------------------------------------------
result2=sum_of_three_num()
print(result2)
result2=sum_of_three_num(n1=10)
print(result2)
result2=sum_of_three_num(n1=10,n2=20)
print(result2)
result2=sum_of_three_num(n1=10,n2=20,n3=30)
print(result2)
