"""
Write a function to calculate and return the range and maximum height of a projectile, taking angle and velocity as arguments. Test it 
with the values velocity = 10 ms-1 and angle = 30 degrees.
"""
import math

def get_range(v, a, g=9.81):
    return (v ** 2) * math.sin(math.radians(2 * a)) / g

def get_height(v, a, g=9.81):
    return (v ** 2) * (math.sin(math.radians(a)) ** 2) / 2 / g

def get_projectile_numbers(velocity, angle):
    range = get_range(velocity, angle)
    height = get_height(velocity, angle)
    return range, height

print("What is the starting velocity in ms^-1: ")
v = float(input())
print("What is the starting angle in degrees: ")
a = float(input())

range, height = get_projectile_numbers(v, a)
print("The range is " + str(round(range, 2)) + " meters and the height is " + str(round(height, 2)) + " meters.")