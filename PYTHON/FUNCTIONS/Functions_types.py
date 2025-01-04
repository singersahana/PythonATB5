# User defined functions
# 1. They don't return -->non return
# 2.They can return something
# 3.They have parameters
# 4.They don't have parameters / arguments

print("------------------------------------------------------------------")


# 1.They don't return anything ---> non return
# No return type and No parameter/ Argument - NRNP

def greet():
    print("HEllO\n")  # there is no return type and no argument as well


greet()

print("------------------------------------------------------------------")


# 2. No return type with argument - NRYP
def greet(name):
    print("Hello", name)


greet("SAHANA")
print("------------------------------------------------------------------")


# 3. No return type with default argument
def say_hello_default_arg(name="Sahana"):
    print("HELLO", name.upper())


say_hello_default_arg("SAANU")
say_hello_default_arg()
print("------------------------------------------------------------------")


# 4.Multiple arguments
def multiple_args(name1="A", name2="B"):
    print("MULTIPLE-->", name1, name2)


multiple_args()
multiple_args(name1="SAHANA", name2="H C")
multiple_args(name1="sahana")
multiple_args(name2="H C")
print("------------------------------------------------------------------")


# 5.Argument with return type
def sum_of_two_no(a, b):
    return a + b


result = sum_of_two_no(3, 4)
print(result)
print("------------------------------------------------------------------")


def sum_of_two_no_with_default_arg(a=100,b=200):
    return a+b
result=sum_of_two_no_with_default_arg(a=30,b=70)
print(result)
sum_of_two_no_with_default_arg()
print(result)
