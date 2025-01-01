# Write a program that calculates and displays the letter grade for a given score
# (eg:, ABCD or F)
# 90-100 -- A
# 80-89 ---B
# 70-79 ---C
# 60-69 ---D
# 0-59 ----F
# --------------------------------------------------------------------------------------

score = int(input("Enter your score\n"))

if score>=90 and score<=100:
    print("YOUR GRADE IS --- A",score)
elif score>=80 and score<=89:
    print("YOUR GRADE IS --- B",score)
elif score>=70 and score<=79:
    print("YOUR GRADE IS --- C",score)
elif score>=60 and score<=69:
    print("YOUR GRADE IS --- D",score)
elif score>100 and score<=-1:
    print("YOU CAN'T GET GRADE! --- OUT OF RANGE")
else:
    print("YOUR GRADE IS --- F",score)