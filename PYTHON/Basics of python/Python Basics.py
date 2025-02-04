
#print(self, *args, sep=' ', end='\n', file=None)
print("Hello World!")
#args ---> specifies that unlimited no of comma separated arguments we can pass inside function
print("My","NAME","SAHANA") # By default its taking only space
#sep ---> specifies that separators we can provide any special characters
print("My","NAME","SAHANA",sep='-')
#end --> it indicates that where it should end
#\n --> New line by default it will be taking next line
print("My","NAME","SAHANA",end=';')
# Indetation ERROR
#     print("hello world")
# we will end up with Indetation errors because python follows PEP 8 standard
# A style guide that provides guidelines for naming conventions, indentation, and comments
print("sahana","age",22,"height",149,"weight",47)