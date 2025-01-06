# Decorators are used before the func or after the func
# It is used for generating reports or log's
# @ is used to add the decorators


def add_security(func):
    def wrapper():
        print("1.Before the func called.")
        print("2.Add helemet,dashcash,gloves,knee gaurds,license")
        func() # driving_scooty or driving_ola
        print("3.After the function is called.")
        print("4.Secure Driving, leave all the items!")
    return wrapper()
@add_security
def driving_ola():
    print("OLA!")


@add_security
def driving_scooty():
    print("NORMAL FUNCTION!")
    print("I am driving scooty!")