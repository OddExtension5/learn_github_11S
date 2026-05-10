#bmi
choice = input("Enter 'mks' to calculate in MKS system or 'is' for Imperial System: " )

if choice=='mks':
    h = float(input("Enter height in metre: "))
    w = float(input("Enter weight in kilogram: "))
    bmi = round((w/(h*h)),4)
else:
    h = float(input("Enter height in inch: "))
    w = float(input("Enter weight in pound: "))   
    bmi = round((w/(h*h))*703,4)

print("BMI:",bmi)
