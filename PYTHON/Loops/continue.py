# continue means skip this statement and go back
for num in range(10):
    if num %2 == 0:
        continue
    else:
        print(num)



# i/p|condition|o/p
# 0  |0%2=0|true --continue --skip
# 1 |1%2 |false -->o/p
# 2 |2%2 |true --continue -->skip
# 3 |3%2 |false -->o/p
# 4 |4%2 |true --continue -->skip
# 5 |5%2 | false -->o/p
# 6 |6%2 |true --continue -->skip
# 7 |7%2 |false -->o/p
# 8 |8%2 |true --continue -->skip
# 9 |9%2 |false -->o/p
# 10 |10%2 |true -->exit the loop

# pass can be used in the statement ,functions,class and objects