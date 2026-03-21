#Polymorphism  means many forms
#when the same operator is allowed to have different meaning according to the context

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def showNumber(self):
        print(self.real, "i +", self.imag, "j")

    def __add__(self, num2): #the dunder function is used to overload the + operator and it takes two parameters the first one is self and the second one is num2 which is the number we want to add to self
        newReal = self.real + num2.real #self.real — This is the real part of the current object (the one you're calling the method on). self always refers to the instance that called the method.  num2.real — This is the real part of the second object that you're adding to it. num2 is the parameter passed to the method—a different Complex object.
        newImag = self.imag + num2.imag
        return Complex(newReal, newImag)
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImag = self.imag - num2.imag
        return Complex(newReal, newImag)
    
num1 = Complex(2, 3)
num1.showNumber()
num2 = Complex(4, 5)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

#if i use dunder function i.e __add__ then i can use num1 + num2 instead of num1.add(num2)  


