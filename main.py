import math
a = 2 * math.sqrt(3)
b = 3
for i in range(100):
    print(i, end=" ")
    a = 2 * a * b / (a + b)
    b = math.sqrt(a * b)
    print(str(a) + " "+ str(b))

print(str(math.pi))