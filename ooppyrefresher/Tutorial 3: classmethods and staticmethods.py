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









