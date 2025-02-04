t = tuple()
print(t)

#conversion list to tuple
t1 = tuple(["bread","butter","milk"])
print(t1)
# tuple within tuple
fav_sweet1=("jamoon","rasmali","jalebi","burfi")
fav_chat1 = ("samosa","masal poori","gobi")
fav_food = (fav_sweet1,fav_chat1)
print(fav_food)
print(fav_food[0])
print(fav_food[0][0])
print(fav_food[1][1])