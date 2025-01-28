import math

g=9.81
# acceleration due to gravity
v0=44
# the initial velocity
y0=1
# height of the barrel (m)
x=0.5
# the horizontal distance travelled
deg=80
# elevation in degree
t= deg * (math.pi / 180)
# formula to convert degrees to radians use

y= y0 + x * math.tan(t) - g * x ** 2 / (g * x **2) / (v0 * math.cos(t) ** 2)
print(y)