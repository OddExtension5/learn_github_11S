#time2
import datetime
s = int(input("Enter no. of seconds: "))

d = s//(24*3600)
s = s%(24*3600)
h = s//3600
s = s%3600
m = s//60
s = s%60

print("D:HH:MM:SS")
print(f"{d}:{h:02}:{m:02}:{s:02}")