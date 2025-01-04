# *args --> unlimited no arguments it will take

def multi_args(*args):
    # *args --> tuple
    for i in args:
        print(i)
multi_args("sahana")
multi_args("sahana","sneha","ambika","chandru")
multi_args("sahana",10,True,"HC")