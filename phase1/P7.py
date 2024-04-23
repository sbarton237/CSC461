"""
Code that finds the gradient of a function at a point. The gradient is a math concept in multivariable calculus, where the partial
derivatives for every variable in a funtion is found. This is a vector that points in the direction of the steepest slope at that point.
It uses object oriented programming to hold the various variables and redefines basic math operations in order to allow for further
manipulation to find the gradient.
"""

from math import e, log
import numpy as np

class Variable:

    def __init__(self, name=None):
        self.name = name #name corresponds with key in values

    def __str__(self):
        return self.name #return name if turned into string or printed
    
    def __add__(self, other):
        return AdditionVariable(self, other)
    
    def __radd__(self, other):
        return AdditionVariable(self, other)
    
    def __sub__(self, other):
        return self + (other * -1)
    
    def __rsub__(self, other):
        return (self * -1) + other
    
    def __mul__(self, other):
        return MultiplicationVariable(self, other)
    
    def __rmul__(self, other):
        return MultiplicationVariable(self, other)
    
    def __truediv__(self, other):
        return self * (other ** -1)
    
    def __rtruediv__(self, other):
        return (self ** -1) * other
    
    def __pow__(self, other):
        return PowVariable(self, other)
    
    def __rpow__(self, other):
        return PowVariable(other, self)
    
    def exp(self):
        return EVariable(self)
    
    def ln(self):
        return LnVariable(self)
    
    def evaluate(self, values):
        return values[self.name] #give the value
    
    def gradient(self, values):
        lst = [0 for i in range(len(values))] #start with 0
        lst[list(values.keys()).index(self.name)] = 1 #set location of variable to 1
        return np.array(lst) #return as np array for easier manipulation
    
class AdditionVariable(Variable):
    
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + " + " + str(self.right)
    
    def evaluate(self, values):
        if issubclass(type(self.right), Variable):
            return self.left.evaluate(values) + self.right.evaluate(values)
        else:
            return self.left.evaluate(values) + self.right
        
    def gradient(self, values):
        if issubclass(type(self.right), Variable):
            return self.left.gradient(values) + self.right.gradient(values)
        else:
            return self.left.gradient(values)
        
class MultiplicationVariable(Variable):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + " * " + str(self.right)
    
    def evaluate(self, values):
        if issubclass(type(self.right), Variable):
            return self.left.evaluate(values) * self.right.evaluate(values)
        else:
            return self.left.evaluate(values) * self.right
        
    def gradient(self, values):
        if issubclass(type(self.right), Variable):
            return self.left.gradient(values) * self.right.evaluate(values) + self.left.evaluate(values) * self.right.gradient(values)
        else:
            return self.left.gradient(values) * self.right
        
class PowVariable(Variable):
    
    def __init__(self, base, pow):
        self.base = base
        self.pow = pow

    def __str__(self):
        return str(self.base) + " ^ " + str(self.pow)
    
    def evaluate(self, values):
        if issubclass(type(self.pow), Variable) and issubclass(type(self.base), Variable):
            return self.base.evaluate(values) ** self.pow.evaluate(values)
        elif issubclass(type(self.pow), Variable):
            return self.base ** self.pow.evaluate(values)
        else:
            return self.base.evaluate(values) ** self.pow
        
    def gradient(self, values):
        if issubclass(type(self.pow), Variable) and issubclass(type(self.base), Variable):
            return self.pow.evaluate(values) * self.base.evaluate(values) ** (self.pow.evaluate(values) - 1) * self.base.gradient(values) + self.base.evaluate(values) ** self.pow.evaluate(values) * log(self.base.evaluate(values)) * self.pow.gradient(values)
        elif issubclass(type(self.pow), Variable):
            return self.base ** self.pow.evaluate(values) * log(self.base) * self.pow.gradient(values)
        else:
            return self.pow * self.base.evaluate(values) ** (self.pow - 1) * self.base.gradient(values)
        
class EVariable(Variable):
    
    def __init__(self, pow):
        self.pow = pow
    
    def __str__(self):
        return "e ^ " + str(self.pow)
    
    def evaluate(self, values):
        return e ** self.pow.evaluate(values)
    
    def gradient(self, values):
        return e ** self.pow.evaluate(values) * self.pow.gradient(values)
    
class LnVariable(Variable):

    def __init__(self, argument):
        self.argument = argument

    def __str__(self):
        return "ln(" + str(self.argument) + ")"
    
    def evaluate(self, values):
        return log(self.argument.evaluate(values))
    
    def gradient(self, values):
        return 1 / self.argument.evaluate(values) * self.argument.gradient(values)
    
x = Variable(name="x")
y = Variable(name="y")
z = Variable(name="z")

p1 = {"x": 1, "y": 2, "z": 3}
p2 = {"x": 6, "y": 4, "z": 2}
p3 = {"x": 12, "y": 13, "z": 6}

eq1 = 2 * x + 3 * y - 5 * z
eq2 = x * y * z + x ** 3 - z / y
eq3 = x.exp() + y.ln() + 1 / z

print(eq1, eq2, eq3, sep="\n")
print()
print("eq1 = " + str(round(eq1.evaluate(p1), 2)) + " at x=1, y=2, z=3")
print("eq1 = " + str(round(eq1.evaluate(p2), 2)) + " at x=6, y=4, z=2")
print("eq1 = " + str(round(eq1.evaluate(p3), 2)) + " at x=12, y=13, z=6")
print()
print("eq2 = " + str(round(eq2.evaluate(p1), 2)) + " at x=1, y=2, z=3")
print("eq2 = " + str(round(eq2.evaluate(p2), 2)) + " at x=6, y=4, z=2")
print("eq2 = " + str(round(eq2.evaluate(p3), 2)) + " at x=12, y=13, z=6")
print()
print("eq3 = " + str(round(eq3.evaluate(p1), 2)) + " at x=1, y=2, z=3")
print("eq3 = " + str(round(eq3.evaluate(p2), 2)) + " at x=6, y=4, z=2")
print("eq3 = " + str(round(eq3.evaluate(p3), 2)) + " at x=12, y=13, z=6")
print()
print("Gradient at x=1, y=2, z=3 for eq1: " + str(eq1.gradient(p1)))
print("Gradient at x=6, y=4, z=2 for eq1: " + str(eq1.gradient(p2)))
print("Gradient at x=12, y=13, z=6 for eq1: " + str(eq1.gradient(p3)))
print()
print("Gradient at x=1, y=2, z=3 for eq2: " + str(eq2.gradient(p1)))
print("Gradient at x=6, y=4, z=2 for eq2: " + str(eq2.gradient(p2)))
print("Gradient at x=12, y=13, z=6 for eq2: " + str(eq2.gradient(p3)))
print()
print("Gradient at x=1, y=2, z=3 for eq3: " + str(eq3.gradient(p1)))
print("Gradient at x=6, y=4, z=2 for eq3: " + str(eq3.gradient(p2)))
print("Gradient at x=12, y=13, z=6 for eq3: " + str(eq3.gradient(p3)))
