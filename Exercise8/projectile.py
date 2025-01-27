import math
# import math module

y0 = 1
x= 0.5
g = 9.81
v0 = 44
deg= 80
t = deg * (math.pi/180)
# defining variables

y = y0 + x*(math.tan(t)) - (g*x**2/ (2*(v0 * math.cos(t))**2))
#writing out equation. I learnt that * is multiply and **is squared

print(y)
