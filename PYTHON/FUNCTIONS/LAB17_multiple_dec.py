# In python we are using decorators in java we called it as annotations

def decorator_1(func):

    def wrapper():
        print("DECORATOR-1")
        func()
    return wrapper

def decorator_2(func):

    def wrapper():
        print("DECORATOR-2")
        func()
    return wrapper

@decorator_1
@decorator_2
def say_hello():
    print("HELLO!")
say_hello()