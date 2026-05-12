#heron's formula
s1 = float(input("Enter side: "))
s2 = float(input("Enter side: "))
s3 = float(input("Enter side: "))

s = (s1+s2+s3)/2
a = (s*(s-s1)*(s-s2)*(s-s3))**0.5

print("Area: ",a)