# program to display area of field in acres

l = float(input("Enter length in feet: "))
b = float(input("Enter breadth in feet: "))

a = (l*b)/43560

print(f"Area: {a} acres")
