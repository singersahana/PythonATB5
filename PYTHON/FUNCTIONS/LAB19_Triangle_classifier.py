#Write a program to classify a triangle based on its length
# Given 3 inputs respective lengths of the triangle
# determine the type of triangle -- Equilateral or Isosceles or scalene


def Clasiify_the_triangle(a,b,c):
    if a>0 and b>0 and c>0:
        if a+b>c and a+c>b and b+c>a:
            if a==b==c:
                return "Equilateral triangle"
            elif a==b or b==c or  a==c:
                return "Isosceles Triangle"
            else:
                return "Scalene Triangle"
        else:
            print("NOT A TRIANGLE")
    else:
        print("YOU HAVE ENTERED INVALID LENGTH")

SideA = float(input("ENTER THE SIDE-A,"))
SideB = float(input("ENTER THE SIDE-B,"))
SideC = float(input("ENTER THE SIDE-C,"))

result = Clasiify_the_triangle(SideA,SideB,SideC)
print(result)