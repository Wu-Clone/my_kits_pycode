# Generate a certain amount of random numbers within a certain range
import random

while True:
    min = int(input("Input min:"))
    max = int(input("Input max:"))
    num = int(input("Input num:"))
    print(random.sample(range(min, max), num))
