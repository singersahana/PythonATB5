#Write a program to classify a triangle based on its length
# Given 3 inputs respective lengths of the triangle
# determine the type of triangle -- Equilateral or Isosceles or scalene

A = float(input("ENTER THE SIDE-A,"))
B = float(input("ENTER THE SIDE-B,"))
C = float(input("ENTER THE SIDE-C,"))

if A == B and B==C and A==C:
    print("ITS IS A EQUILATERAL TRIANGLE\n")
elif A == B and B ==A and A!=C:
    print("ITS IS A ISOSCELES TRIANGLE\n")
else:
    print("ITS IS A SCALENE TRIANGLE\n")