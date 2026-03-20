# OOPS concept of python
class Car:
    color = "Red"
    brand = "Toyota"

c1 = Car()   # c1 is an object of class Car
print(c1.color) # Red
print(c1.brand) # Toyota  

class Student:
    college = "ABC College" #class attribute
    def __init__(self, fullname, marks):  # constructor is a special method that is called when an object is created #self parameter is used to refer to the current object of the class and access the attributes and methods of the class
        self.name = fullname  # name is an attribute of the class Student and it is initialized to "John" when an object of the class is created
        self.marks = marks #object attribute

    def hello(self):# method of the class Student
        print("Hello, World!",self.name) # Hello, World! John
    def get_marks(self):# method to get the marks of the student
        print("Marks:", self.marks) # Marks: 85
        
        print("Adding new student")

s1 = Student("John", 85)  #s1 is an object of class Student 
print(s1.name) # John
print(s1.marks) # 85
s1.hello() # Hello, World! John

s2 = Student("Jane", 90)
print(s2.name) # Jane
print(s2.marks) # 90
print(s2.college) # ABC College
s2.hello() # Hello, World! Jane
s2.get_marks()


#Abstraction (hide implementation deatils)

class Car:
    def __init__(self):
        self.acc= False
        self.brake = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.brake = False
        self.clutch = True
        print("Car started")

car1 = Car()
car1.start() # Car started IT TELLS ONLY MAIN FUNCTION







         