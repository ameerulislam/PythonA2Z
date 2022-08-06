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
    
class Developer(Employee):
    raise_amt = 1.10


dev_1 = Developer('Ameer', 'Ul Islam', 50000)
dev_1_1 = Employee('Ameer', 'Ul Islam', 50000)
dev_2 = Developer('Kazol', 'Akter', 60000)

print(dev_1.email)
print(dev_2.email)

# print(help(Developer)) # this will print out all info about the Developer class. Where it was inherited from methods etc
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_1_1.pay)
dev_1_1.apply_raise()
print(dev_1_1.pay)