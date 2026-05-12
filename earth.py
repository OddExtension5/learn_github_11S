# latitude longitude
import math
import numpy as np
t1 = float(input("Enter latitude of 1st point: "))
g1 = float(input("Enter longitude of 1st point: "))
t2 = float(input("Enter latitude of 2nd point: "))
g2 = float(input("Enter longitude of 2nd point: "))

t1 = math.radians(t1)
g1 = math.radians(g1)
t2 = math.radians(t2)
g2 = math.radians(g2)

dist = 6371.01*np.arccos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))

print(f"Distance: {dist} km")