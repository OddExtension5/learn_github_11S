#wci
t = float(input("Enter temperature in celcius: "))
v = float(input("Enter wind speed in km/hr: "))

wci = 13.12+0.6215*t-11.37*v**0.16+0.3965*t*v**0.16
wci = round(wci)

print("WCI:",wci)