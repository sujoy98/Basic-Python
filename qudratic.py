# cmath is for importing complex math module
import cmath
a = int(input('Enter a '))
b = int(input('Enter b '))
c = int(input('Enter c '))
d = (b**2) - (4*a*c)
sol1 = (-b+ cmath.sqrt(d)) / (2*a)
sol2 = (-b- cmath.sqrt(d)) / (2*a)
print(sol1)
print(sol2)