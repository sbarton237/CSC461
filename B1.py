"""
Assume the population of Florida sandhill cranes grows by 1.94% annually. If we start with a population of 425 birds, how 
large will the population be after a given number of years? Write a program that computes and prints the population sizes for 
a given number of years.
"""

print("Enter the number of years after the start: ", end="")
years = int(input())
start = 425

def find_pop(start, years):
    for i in range(years):
        start *= 1.0194
    return int(start)

pop = find_pop(start, years)
print("After " + str(years) + " years there will be " + str(pop) + " birds.")