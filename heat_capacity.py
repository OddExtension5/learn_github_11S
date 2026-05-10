# heat capacity
m = float(input("Enter mass in gram: "))
dt = float(input("Enter change in temperature in Celcius: "))
c = 4.186

q = m*c*dt                               #in joules
Q = round((2.78*10**-7)*q,4)             #in kwh
cost = 8.9*Q

print("Heat energy: ", q)
print(f"Cost:{cost}/-")