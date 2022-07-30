# declare first add attributes later method
from more_itertools import strip
from yaml import full_load


class Employee:
    pass

# instanciating 2 instances of Employees object with no attributes or methods
emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.firstN = "Ameer"
emp_1.lastN = "Ul Islam"
emp_1.email = "example@example.com"
emp_1.pay = 200000

emp_2.firstN = "Raees"
emp_2.lastN = "Ul Islam"
emp_2.email = "example2@example.com"
emp_2.pay = 300000

print(emp_1.email)
print(emp_2.email)

# Now will do it in a better way.  We will iniate these 

class Employee1:
    #self here is basically passing the instance itself automatically by python when creating the instance https://www.youtube.com/watch?v=oaiQ5hYKHTE
    def __init__(self, first, last, pay): 
        self.first = first
        self.fname = first # this one same as the previous one self.first
        self.last = last
        self.pay = pay
        self.email = (first+ '.' + last + '@example.com').replace(' ', '') # you can write logics like this here
    
    def fullname(self): 
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee1('Ameer', 'Ul Islam', 200000)
emp_2 = Employee1('Raees','Ul Islam', 500000)

print(emp_1)
print(emp_2)
print(emp_1.email)
print(emp_2.email)
print(emp_1.first)
print(emp_1.fname) # this one same as the previous one self.first

print(emp_1.fullname())
# another way to call function
print(Employee1.fullname(emp_2)) # this emp_2.fullname() actually gets transformed to Employee1.fullname(emp_2) behind the scenes