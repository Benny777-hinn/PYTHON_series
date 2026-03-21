#OOPs concpert part 2

#del keyword is used to delete the object created by class
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

s1 = Employee("John", 30)
print(s1.name) # Output: John

del s1 # deleting the object s1
print(s1.name) # This will raise an error because s1 has been deleted

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

a1=Account(12345,"password123")

print(a1.acc_no) # Output: 12345
print(a1.__acc_pass) # This will raise an error because __acc_pass is a private variable    


class Person:
    __name = "John" # protected variable

    def __hello(self):
        print("Hello, World!") # private method

    def greet(self):
        self.__hello() # calling the private method within the class

p1 = Person()
print(p1.greet()) # This will print "Hello, World!" and not raise an error


# Inheritence
# means one class can inherit the properties and methods of another class. The class that inherits is called the child class or subclass

# single inheritence
class Car:
    color = "Red" # class variable These properties and methods are shared by all instances of the class or child classes
    @staticmethod #static method is a method that belongs to the class rather than an instance of the class. It can be called on the class itself, rather than on an instance of the class. Static methods are defined using the @staticmethod decorator and do not take self as the first parameter. 
    def start ():
        print("Car is starting...")

    @staticmethod
    def stop():
        print("Car is stopping...")

class ElectricCar(Car):
    def __init__(self,name):
        self.name=name

car1 = ElectricCar("Tesla")
car2 = ElectricCar("Nissan Leaf")

print(car1.color) # Output: Tesla  here we are able to access the class variable color from the parent class Car
        
#multi level inheritence

class Car:
    color = "Red" # class variable These properties and methods are shared by all instances of the class or child classes
    @staticmethod
    def start ():
        print("Car is starting...")

    @staticmethod
    def stop():
        print("Car is stopping...")

class ElectricCar(Car):
    def __init__(self,name):
        self.name=name

class Tesla(ElectricCar):
    def __init__(self, type,name):
        self.type = type
        self.name = name

car1 = Tesla("Model S", "Tesla Model S")
print(car1.color) # Output: Red here we are able to access the class variable color
print(car1.type) # Output: Model S
print(car1.name) # Output: Tesla Model S

# multiple inheritence

class A:
    varA = "Variable A"

class B:
    varB = "Variable B"

class C(A, B):
    varC = "Variable C"

c1 = C() # creating an object of class C which inherits from both class A and class B
print(c1.varA) # Output: Variable A
print(c1.varB) # Output: Variable B
print(c1.varC) # Output: Variable C

#super() function is used to call the parent class constructor
class Car:
    def __init__(self, color):
        self.color = color
class ElectricCar(Car):
    def __init__(self, color, name):
        super().__init__(color) # calling the parent class constructor
        self.name = name
car1 = ElectricCar("Red", "Tesla Model S")
print(car1.color) # Output: Red here we are able to access the class variable color from the parent class Car
print(car1.name) # Output: Tesla Model S


#class method is a method that is bound to the class and not the instance of the class. It can modify the class state that applies across all instances of the class, rather than just a single instance. Class methods are defined using the @classmethod decorator and take cls as the first parameter instead of self.

class Person:
    name = "John" # class variable

    @classmethod
    def change_name(cls, name):
        cls.name = name # modifying the class variable name

p1 = Person()
p1.change_name("Alice") # changing the class variable name using the class method
print(p1.name) # Output: Alice here we are able to access the modified class variable name
print(Person.name) # Output: Alice here we are able to access the modified class variable name using the class name as well

#Property decorator is used to define a method as a property. A property is a special kind of attribute that computes its value when accessed. It allows us to define methods that can be accessed like attributes, without needing to call them as functions.

class Student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
    
    @property
    def percentage(self):
        total_marks = self.phy + self.chem + self.maths
        percentage = (total_marks / 300) * 100
        return percentage 
    # or we can write return str((self.phy + self.chem + self.maths) / 300 * 100) + "%"

s1 = Student(85, 90, 95)
print(s1.percentage) # Output: 90.0 here we are able to access
#now if we change marks of any subject then...
s1.phy = 80
print(s1.percentage) # Output: 88.33333333333333 will be changed

#This method is used because if we change the marks of any ssubject without property method we cannot get updated percentage but with property method we can get updated percentage without calling the method as a function. We can access it like an attribute.

