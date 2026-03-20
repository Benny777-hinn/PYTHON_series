#Practice question 1: Create a class called Student that has two attributes: name and marks. The class should have a method called get_avg that calculates and returns the average of the marks. Create an object of the Student class and call the get_avg method to display the average marks.

class Student:
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks 
    
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name, "Average marks is", sum/len(self.marks))# or sum/3

s1 = Student("John",[85,100,90] )
s1.get_avg()

s1.name="Benny"
s1.get_avg()



class Account:
    def __init__(self, bal,acc):
        self.balance = bal
        self.account_no = acc
    
    def debit(self, amount):
        self.balance -= amount
        print("Debited amount:", amount)
        print("Current balance:", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("Credited amount:", amount)
        print("Current balance:", self.balance)

    def get_balance(self):
        print("Current balance:", self.balance)


acc1= Account(1000, "1234567890")
print(acc1.balance) # 1000
print(acc1.account_no) # 1234567890

acc1.debit(200) # Debited amount: 200 Current balance: 800
acc1.credit(500) # Credited amount: 500 Current balance: 1300
acc1.get_balance() # Current balance: 1300

