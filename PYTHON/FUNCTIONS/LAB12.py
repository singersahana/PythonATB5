def outer_function():
    var1 =30 # according to logic it is local variable but for the below two functions it will be
    # acting as global variables

    def inner_function():
        var2 = 20
        print(var1)

    def inner_function1():
        print(var1)

    # print(var2) # inner local variable we can't able to access outside the function
    inner_function()
    inner_function1()
outer_function()