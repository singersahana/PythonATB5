my_list = [1, 2, 3]
# indexing
print("Element at the index 0 -", my_list[0])
print("Element at the index 1 -", my_list[1])
print("Element at the index 2 -", my_list[2])

# =====================================================================
# append()--> append the object at the end of the list
# append doesn't takes list
my_list.append(4)
my_list.append(5)
print(my_list)
# =====================================================================
# extend() ---> append a new list
# it will take list
my_list.extend([6, 7, 8])
print(my_list)
# =====================================================================
# insert() --->
my_list.insert(1, "Sahana")
print(my_list)
print(len(my_list))

my_list.insert(0, 0)
print(my_list)
# =====================================================================
my_list[1] = "HC"
print(my_list)
my_list.remove("HC")
print(my_list)

# =====================================================================
my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)
# -------------------------------------------------------------------
my_list.remove("Sahana")
my_copy_list.remove("Sahana")
my_list.sort()
my_copy_list.sort()
