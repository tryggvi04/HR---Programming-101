import math
a_str = input() # Do not change this line.
b_str = input() # Do not change this line.
c_str = input() # Do not change this line.

#Breytum str yfir í heiltölum
a_int = int(a_str)
b_int = int(b_str)
c_int = int(c_str)

#Finnum s
s = (a_int + b_int + c_int)/2

#nú notum við formúluna til að finna svarið
area = math.sqrt(s * (s - a_int) * (s - b_int) * (s - c_int))
print(area) # Change this line at your own peril.