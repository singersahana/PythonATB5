# # import math
# # def give_me_pow(num):
# #     return math.pow(num,2)
# # op = give_me_pow(10)
# # print(op)
# import math
#
# op = lambda num : math.pow(num,2)
# print(op(10))
#
# # ------------------------
import math

op1=lambda : math.pow(int(input("enter the number\n")),2)
print(op1())