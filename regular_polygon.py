#regular_polygon
import math
n = int(input("Enter no. of sides: "))
s = float(input("Enter length of each side: "))

area = (n*s**2)/4*math.tan(math.radians(180)/n)
area = round(area,2)

print("Area: ", area)