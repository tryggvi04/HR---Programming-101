
import math
d = input() # Change this line at your own peril.

# reiknum radíus
r = float(d)/2

#reiknum volume á kúlu
v = 4/3 * math.pi * math.pow(r, 3)

#deilum því í helming
volume_of_half_sphere = v/2


print(volume_of_half_sphere)