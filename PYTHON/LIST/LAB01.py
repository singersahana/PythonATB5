# Advanced data types
# LIST
# Tuple
# SET
# Dictionary
#--------------------------------------
# LIST
# list is a collection of items
# Duplicates are allowed
# Multiple data types are allowed
# start from the index -0 ....,len-1
# syntax -[]
# ----------------------------------------
# grocery list - bread,banana,butter,paneer
# Marks_list-85,88,90,98,67

my_list = [1,2,3] # same data type -- (int)
my_list2= [1, True,"Sahana",4.10]
print(my_list)
print(len(my_list))
print(my_list2)
print(len(my_list2))
print(my_list[0],my_list[1],my_list[2],sep="|")
# print(my_list[3])
print("-------------------------------------------------")
# iterate using for loop
for item in my_list2:
    # print(item)
    print(item,end=" ")