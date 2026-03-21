# Practice question 1: in the following code, create a class called Circle with an attribute radius and two methods area and perimeter. The area method should return the area of the circle, and the perimeter method should return the perimeter of the circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius

c1= Circle(24)
print(c1.area())
print(c1.perimeter())

# Practice question 2: Create a class called Employee with attributes role, dept and salary. Create a method called showDetails that prints the details of the employee. Then create a subclass called Engineer that inherits from Employee and has additional attributes name and age. Override the showDetails method in the Engineer class to include the name and age of the engineer along with the role, dept and salary. 


class Employee:
    def __init__(self, role,dept , salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role:", self.role)
        print("Department:", self.dept)
        print("Salary:", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "R&D", 70000) #super() is used to call the constructor of the parent class Employee and pass the values for role, dept and salary. This way we can reuse the code of the parent class and avoid duplication.basically inheritance is allowed...

e1 = Employee("Manager", "Sales", 50000)
e1.showDetails()

eng1 = Engineer("Alice", 30)
eng1.showDetails()

# Practice question 3: Is operator overloading possible in Python? If yes, then create a class called Order with attributes item and price. Overload the > operator to compare the price of two orders and return True if the price of the first order is greater than the second order, otherwise return False.


class Order:
    def __init__(self, item,price):
        self.item = item
        self.price = price
    
    def __gt__(self, od2):
        return self.price > od2.price
    
order1 = Order("Laptop", 1000)
order2 = Order("Phone", 500)

print(order1 > order2) # True because 1000 is greater than 500

# we can change the operator > to < or == and it will work according to the logic we have defined in the dunder function __gt__ or __lt__ or __eq__ respectively. This is called operator overloading and it is a form of polymorphism.
        



