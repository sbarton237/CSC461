"""
Go find my physics notebook, find something that looks like it could be challenging to code, and do it. Probably do E&M because that's 
more fun. Go for electric fields because then we might get to do some integration and that's hard but that's fun. That, or do something
related to differentiation.
"""

#Problem 1: Get velocity and acceleration at a point from position formula

from math import e, log
import numpy as np

class Variable: 
    
    def __init__(self, name=None):
        self.name = name
        #give variable a name that corresponds with its key in values
        
    def __str__(self):
        return self.name
        #when turned into a string or printed, give the name of the variable
        
    def __add__(self, other):
        return AdditionVariable(self, other)
        #make a variable for addition adding this variable and the other element
        
    def __radd__(self, other):
        return AdditionVariable(self, other)
        #make a variable for addition adding this variable and the other element

    def __sub__(self, other):
        return self + (other * -1)
        #subtract by adding the negative version of the other element to this variable
        
    def __rsub__(self, other):
        return (self * -1) + other
        #subtract by adding the negative version of this variable to the other element
    
    def __mul__(self, other):
        return MultiplicationVariable(self, other)
        #make a variable for multiplication multiplying this variable and the other element
        
    def __rmul__(self, other):
        return MultiplicationVariable(self, other)
        #make a variable for multiplication multiplying this variable and the other element
        
    def __truediv__(self, other):
        return self * (other ** -1)
        #divide by multiplying the reciprocal of the other element to this variable
    
    def __rtruediv__(self, other):
        return (self ** -1) * other
        #divide by multiplying the reciprocal of this variable to the other element
        
    def __pow__(self, other):
        return PowVariable(self, other)
        #make a variable for exponentiation of this variable to the other element
        
    def __rpow__(self, other):
        return PowVariable(other, self)
        #make a variable for exponentiation of the other element to this variable
        
    def exp(self):
        return EVariable(self)
        #make a variable for raising e to this variable
        
    def log(self):
        return LogVariable(self)
        #make a variable for taking the natural log of this variable
        
    def evaluate(self, values):
        return values[self.name]
        #return the value of this variable from the values dictionary
        
    def gradient(self, values):
        lst = [0 for i in range(len(values))]
        #create a list as long as the number of values (inputs) and set all elements to 0
        lst[list(values.keys()).index(self.name)] = 1
        #set the location of the variable in values to 1
        return np.array(lst)
        #return as a numpy array for better manipulation later
    
    def differentiate(self, values):
        return 1
    
class AdditionVariable(Variable):
    
    def __init__(self, left, right):
        self.left = left #one of the variables being added
        self.right = right #one of the variables/numbers being added
        
    def __str__(self):
        return str(self.left) + " + " + str(self.right)
        #when turned into a string or printed, give the string of the left plus the string of the right
    
    def evaluate(self, values):
        if issubclass(type(self.right), Variable): #if right is variable
            return self.left.evaluate(values) + self.right.evaluate(values)
            #add the evaluation of the left variable and the evaluation of the right variable
        else: #else
            return self.left.evaluate(values) + self.right
            #add the evaluation of the left variable and the right number
            
    def gradient(self, values):
        if issubclass(type(self.right), Variable): #if right is variable
            return self.left.gradient(values) + self.right.gradient(values)
            #add the gradient of the left variable and the gradient of the right variable
        else: #else
            return self.left.gradient(values)
            #return the gradient of the left variable
        
    def differentiate(self, values):
        if issubclass(type(self.right), Variable):
            return str(self.left.differentiate(values)) + " + " + str(self.right.differentiate(values))
        else:
            return self.left.differentiate(values)
        
class MultiplicationVariable(Variable):
    
    def __init__(self, left, right):
        self.left = left #one of the variables being multiplied
        self.right = right #one of the variable/numbers being multiplied
        
    def __str__(self):
        return str(self.left) + " * " + str(self.right)
        #when turned into a string or printed, give the string of the left times the string of the right
        
    def evaluate(self, values):
        if issubclass(type(self.right), Variable): #if right is variable
            return self.left.evaluate(values) * self.right.evaluate(values)
            #multiply the evaluation of the left variable and the evaluation of the right variable
        else: #else
            return self.left.evaluate(values) * self.right
            #multiply the evaluation of the left variable and the right number
    
    def gradient(self, values):
        if issubclass(type(self.right), Variable): #if right is variable
            return self.left.gradient(values) * self.right.evaluate(values) + self.left.evaluate(values) * self.right.gradient(values)
            #multiply the gradient of the left by the evaluation of the right and add to the gradient of the right times the evaluation of the left
        else: #else
            return self.left.gradient(values) * self.right
            #multiply the gradient of the left by the value of the right
        
    def differentiate(self, values):
        if issubclass(type(self.right), Variable):
            return str(self.left.differentiate(values) * self.right.name) + " + " + str(self.right.differentiate(values) * self.left.name)
        else:
            return self.left.differentiate(values) * self.right

class PowVariable(Variable):
    
    def __init__(self, base, exp):
        self.base = base #variable/number representing the base
        self.exp = exp #variable/number representing the exponent
    
    def __str__(self):
        return str(self.base) + " ^ " + str(self.exp)
        #when turned into a string or printed, give the string of the base to the string of the exponent
    
    def evaluate(self, values):
        if issubclass(type(self.exp), Variable) and issubclass(type(self.base), Variable): #both parts are variables
            return self.base.evaluate(values) ** self.exp.evaluate(values)
            #set the evaluation of the base to the power of the evaluation of the exponent
        elif issubclass(type(self.exp), Variable): #if only exponent a variable
            return self.base ** self.exp.evaluate(values)
            #set the value of the base to the power of the evaluation of the exponent
        else: #only base is variable
            return self.base.evaluate(values) ** self.exp
            #set the evaluation of the base to the pwoer of the value of the exponent
            
    def gradient(self, values):
        if issubclass(type(self.exp), Variable) and issubclass(type(self.base), Variable): #both parts are variables
            return self.exp.evaluate(values) * self.base.evaluate(values) ** (self.exp.evaluate(values) - 1) * self.base.gradient(values) + self.base.evaluate(values) ** self.exp.evaluate(values) * log(self.base.evaluate(values)) * self.exp.gradient(values)
            #do the differentiation for if base is variable and exponent is variable
        elif issubclass(type(self.exp), Variable): #if only the exponent is a variable
            return self.base ** self.exp.evaluate(values) * log(self.base) * self.exp.gradient(values)
            #just do differention for exponent is variable
        else: #only base is variable
            return self.exp * self.base.evaluate(values) ** (self.exp - 1) * self.base.gradient(values)
            #just do differention for base is variable
        
    def differentiate(self, values):
        if issubclass(type(self.exp), Variable) and issubclass(type(self.base), Variable):
            return self.exp.evaluate(values) * self.base.evaluate(values) ** (self.exp.evaluate(values) - 1) * self.base.differentiate(values) + self.base.evaluate(values) ** self.exp.evaluate(values) * log(self.base.evaluate(values)) * self.exp.differentiate(values)
        elif issubclass(type(self.exp), Variable):
            return self.base ** self.exp.evaluate(values) * log(self.base) * self.base.differentiate(values)
        else:
            return self.exp * self.base.evaluate(values) ** (self.exp - 1) * self.base.differentiate(values)
        
class EVariable(Variable):
    
    def __init__(self, exp):
        self.exp = exp #variable representing the exponent
        
    def __str__(self):
        return "e ^ " + str(self.exp)
        #when turned into a string or printed, give e to string of the exponent
        
    def evaluate(self, values):
        return e ** self.exp.evaluate(values)
        #set e to the power of the evaluation of the exponent
        
    def gradient(self, values):
        return e ** self.exp.evaluate(values) * self.exp.gradient(values)
        #set e to the power of the evaluation of the exponent and multiply by the gradient of the exponent

class LogVariable(Variable):
    
    def __init__(self, argument):
        self.argument = argument #variable representing the argument
        
    def __str__(self):
        return "log(" + str(self.argument) + ")"
        #when turned into a string or printed, give log(string of the argument)
    
    def evaluate(self, values):
        if self.argument.evaluate(values) == 0:
            return 10 ** 100
        return log(self.argument.evaluate(values))
        #take the natural log of the argument
        
    def gradient(self, values):
        return 1 / self.argument.evaluate(values) * self.argument.gradient(values)
        #multiply the reciprocal of the evaluation of the argument by the gradient of the argument

x = Variable(name="x")
y = Variable(name="y")
point = {"x": 2, "y": 3}
position = x * x * x
velocity = position.differentiate(point)
acceleration = velocity.differentiate(point)