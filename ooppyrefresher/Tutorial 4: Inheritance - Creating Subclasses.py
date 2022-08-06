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

class Dev(Employee):
    pass

class Developer(Employee):
    raise_amt = 1.10
    # extending the developer class with more features use the init
    def __init__(self, first, last, pay, prog_lang):
        # with super KW below will let the parent class Employee handle the first, last and pay arguments as above
        super().__init__(first, last, pay)
        # The following is another way to initiate the argument but this is less maintainable ie less dynamic more hard coded.
        # Employee.__init__(first, last, pay)
        # this is Developer class specific so Developer class has to handle this
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None): #employees=None because you shouldn't add mutable data types (list/dict etc) as default argument as best practice
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Dev('Ameer', 'Ul Islam', 50000)
dev_1_1 = Employee('Ameer', 'Ul Islam', 50000)
dev_2 = Dev('Kazol', 'Akter', 60000)

print(dev_1.email)
print(dev_2.email)

# print(help(Developer)) # this will print out all info about the Developer class. Where it was inherited from methods etc
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_1_1.pay)
dev_1_1.apply_raise()
print(dev_1_1.pay)

# extending the developer class with more features
dev_1 = Developer('Ameer', 'Ul Islam', 50000, 'Python')
dev_2 = Developer('Kazol', 'Akter', 60000, 'HTML')

print(dev_1.email)
print(dev_1.prog_lang)

mgr_1 = Manager('Sue', 'Smith', 9000, [dev_1] )
mgr_1.print_emps()
mgr_1.add_emp(dev_2)
mgr_1.print_emps()