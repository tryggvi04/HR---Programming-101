
import math
x1_str = input() # Do not change this line.
y1_str = input() # Do not change this line.
x2_str = input() # Do not change this line.
y2_str = input() # Do not change this line.


#Breytum breytanum yfir í floats
x1_float = float(x1_str)
x2_float = float(x2_str)
y1_float = float(y1_str)
y2_float = float(y2_str)

#Nú notum við fjarlægða formúluna til að reikna svarið
d = math.sqrt(math.pow((x2_float - x1_float), 2) + math.pow((y2_float-y1_float), 2))


print(d) # Change this line at your own peril.

