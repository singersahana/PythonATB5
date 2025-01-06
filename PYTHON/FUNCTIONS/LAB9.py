pb_global_b = 12 # global variable
def my_function():
    pb_a = 10
    print(pb_a) # Local variable
    print(pb_global_b)
# print(pb_a) # we cannot local variable outside the function
print(pb_global_b) # we can use the global variables outside the function
my_function()