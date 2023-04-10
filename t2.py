import math

a = math.sqrt(2)
b = 2
for i in range(100):
    b *= 2
    b /= a
    a = math.sqrt(a+2)
    print(b)