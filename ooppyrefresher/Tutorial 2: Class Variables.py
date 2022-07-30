# Instance Variables and Class variables
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

emp_1 = Employee('Ameer', 'Ul Islam', 200000)
emp_2 = Employee('Raees','Ul Islam', 500000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# .__dict__ stuff, to help in Debugging
print(Employee.__dict__)
print(emp_1.__dict__)
print(emp_2.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# raise_amount is inharited from the Class to instance
Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.raise_amount = 1.06 # this is actually creating .raise_amount attribute within emp_1

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_1.__dict__)
print(emp_2.raise_amount)
print(emp_2.__dict__)

# Printing the number of employees directly from the class object after couple of instances got created
print(Employee.num_of_emps)