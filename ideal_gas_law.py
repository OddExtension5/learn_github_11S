#ideal gas law
p = float(input("Enter pressure in Pa: "))
v = float(input("Enter volume in L: "))

choice = input("Enter C for celcius or F for fahrenheit: ")

if choice=='C':
    t = float(input("Enter temperature in celcius: "))
    t = 273.15+t
else:
    t = float(input("Enter temperature in fahrenheit: "))
    t = ((t-32)*5/9)+273.15

n =(p*v*10**-3)/(8.314*t)   #converting L to cubic metre

print("No. of moles: ",n)