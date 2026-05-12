#time
d = int(input("Days: "))
h = int(input("Hours: "))
m = int(input('Minutes: '))
s = int(input("Seconds: "))

s = s + 60*m + 3600*h + 24*3600*d

print("Total seconds: ",s)