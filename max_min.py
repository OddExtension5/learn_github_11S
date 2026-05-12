#max_min
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

maximum = max(a,b,c)
minimum = min(a,b,c)
mid = a+b+c-maximum-minimum

print("Max: ",maximum)
print("Min: ",minimum)
print("Middle: ",mid)
