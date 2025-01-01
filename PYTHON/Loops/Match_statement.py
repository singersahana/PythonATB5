# Match statement --> switch in java
# Match is op and execute
# python >3.10
# --------------------------------------
# match pattern:
#   match variable :
#       case1:
#           code
#       case2:
#           code
# -------------------------------------------
# Write a program to ask the user in which browser he want to execute the automation
browser = input("Enter your browser name\n")
match browser:
    case "firefox":
        print("starting firefox!!!")
    case "chrome":
        print("execute in chrome")
    case "edge":
        print("execute in edge")
    case "safari_browser":
        print("execute in safari browser")
    case _:
        print("browser couldn't find!")

