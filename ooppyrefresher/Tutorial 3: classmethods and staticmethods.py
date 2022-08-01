# Regular Methods Vs Class methods Vs static methods
##########
# regular methods in a class automatically take the instance as the first argument and by convention we were calling this
# self so if a regular method automatically takes in the instance as the first argument then how can we
# change this so that it instead automatically takes the class as the first argument

class Employee:

    # class variables / attributes
    raise_amount = 1.04
    num_of_emps = 0

    #self here is basically passing the instance itself automatically by python when creating the instance https://www.youtube.com/watch?v=oaiQ5hYKHTE
    def __init__(self, first, last, pay): 
        self.first = first
        self.fname = first # this one same as the previous one self.first
        self.last = last
        self.pay = pay
        self.email = (first+ '.' + last + '@example.com').replace(' ', '') # you can write logics like this here
        Employee.num_of_emps += 1 #We're using Class Name instead of self, because this will not be overriden by instances
    
    def fullname(self): 
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount) # this is one way to do it, using the Class Name
        self.pay = int(self.pay * self.raise_amount) # this is another way to do it, using the Class Name
    
    # to do that we're going to use class methods and to turn a regular method into a class method it's as easy as adding a decorator to the top called class method
    @classmethod # Decorator is altering the functionality of our method to where now we receive the class as our first argument instead of the instance
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod #we're use this as alternative consturctor
    def from_string(cls, emp_str):
        first, last , pay = emp_str.split('-')
        return cls(first, last, pay)

emp_1 = Employee('Ameer','Ul Islam', 200000)
emp_2 = Employee('Raees','Ul Islam', 500000)    

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.set_raise_amount(1.05) #this is equivalent to Employee.raise_amount = 1.05 , but now we're using class method set_raise_amount
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.set_raise_amount(1.06) #If you use instance it will work the same as well but this is unlikely to be used
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# class methods as alternative constructors
# The limitation example below
emp_str_1 = 'John-Doe-7000'
emp_str_2 = 'Ameer-UlIslam-2000000'
emp_str_3 = 'Kajol-Akter-2020202'

first, last , pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)

print(new_emp_1.email)
print(new_emp_1.pay)

# The solution example below where we're using class method to do the splitting and creating a new employee object
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
