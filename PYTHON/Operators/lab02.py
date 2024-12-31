# Write a program to cal the area of circle using the formula
# Given its radius
# Area = π*r^2 [take pi = 3.14]

# Logic building formula
# --------------------------
# ||Step 1||
#  figure out input and the output
# input --> r --->radius [datatype is float]
# pi -->3.14
# pow -->** | math.pow
# --------------------
# ||Step 2||
# rough logic---> area = 3.14 * pow(r,2)
# ------------------------
radius = float(input("Enter the radius of the circle\n"))
print(radius)
Area = 3.14 * (radius**2)
print(Area)
# -------------------------------------
# * ----> mul
# **----->power
