set1 ={1,2,3}
set2={4,5,6}
my_set =set1.union(set2)
print(my_set)

print("==========================================")

set3={1,2,3,4}
set4={3,4,5,6}
my_set1=set3.intersection(set4)
print(my_set1)

print("==========================================")
set_diff1=set3.difference(set4)
print(set_diff1)
set_diff2=set4.difference(set3)
print(set_diff2)
print("==========================================")