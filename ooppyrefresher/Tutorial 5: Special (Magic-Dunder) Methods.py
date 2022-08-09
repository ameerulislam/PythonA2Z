# Behavior is different according to object type
# print(1+2) # will do addition
# print('a'+'b') # will do concatination
class Employee: 

    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last
        self.email = (first+ '.' + last + '@example.com').replace(' ', '')
        self.pay = pay
    
    def fullname(self): 
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt) 

    # __repr__ is a fallback method for __str__
    # The goal of __repr__ is to be unambiguous
    # __repr__ is for developers for debugging, you could literally get the code that implemented that output.
    def __repr__(self): 
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
    
    # The goal of __str__ is to be readable
    # def __str__(self):
    #     pass

emp_1 = Employee('Ameer', 'Ul Islam', 200000)

print(emp_1) #output -> <__main__.Employee object at 0x7f3cfa617d00>

# repr(emp_1)
# str(emp_1)