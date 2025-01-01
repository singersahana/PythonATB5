# Problem find the maximum b/w three numbers

num1 = int(input("Enter the number1\n"))    #5
num2 = int(input("Enter the number2\n"))    #3
num3 = int(input("Enter the number3\n"))    #2

# 5 >3 and 5>2 --->5
# num1>num2 and num1>num3 ---> num1

# num2>num1 and num2>num3 ---> num2

# num3 will maximum

if num1>num2 and num1>num3 :
    print("num1 is maximum\n",num1)
elif num2>num1 and num2>num3 :
    print("num2 is maximum\n",num2)
else:
    print("num3 is maximum\n",num3)