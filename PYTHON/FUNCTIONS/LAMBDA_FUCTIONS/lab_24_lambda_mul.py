# Write a program to calculate even and odd

# def find_even_and_odd(num):
#      if num % 2 ==0:
#          print("EVEN NUMBER!")
#      else:
#          print("ODD NUMBER!")
# find_even_and_odd(9)

n = int(input("ENTER A NUMBER\n"))
result = lambda num: "EVEN" if num%2==0 else "ODD"
print(result(n))