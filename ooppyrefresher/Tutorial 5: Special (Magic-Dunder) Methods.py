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
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other): # This is cool, self is an instance of that object and other is another instance of that object
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Ameer', 'Ul Islam', 200000)
emp_2 = Employee('Raees', 'Ul Islam', 100000)

print(emp_1) #output -> <__main__.Employee object at 0x7f3cfa617d00>

print(repr(emp_1))
print(str(emp_1))
#Below is same as above.
print(emp_1.__repr__())
print(emp_1.__str__())

# The following two are the differnt ways of doing the same thing
print(1+2)
print(int.__add__(1,2))
# this str add does concatination
print(str.__add__('1','2'))
print(str.__add__('a','b'))

# The code below is amazing. It's using the dunder __add__ method of that object when we are adding two instance of that Employee object
print(emp_1 + emp_2)

print(len('test'))
print('test'.__len__())

print(len(emp_1))  #if __len__ wasn't defined above this wouldn't have worked

# for more cool stuff similar to above
# https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
# 3.3.8. Emulating numeric types
# The following methods can be defined to emulate numeric objects. Methods corresponding to operations that are not supported by the particular kind of number implemented (e.g., bitwise operations for non-integral numbers) should be left undefined.

# object.__add__(self, other)
# object.__sub__(self, other)
# object.__mul__(self, other)
# object.__matmul__(self, other)
# object.__truediv__(self, other)
# object.__floordiv__(self, other)
# object.__mod__(self, other)
# object.__divmod__(self, other)
# object.__pow__(self, other[, modulo])
# object.__lshift__(self, other)
# object.__rshift__(self, other)
# object.__and__(self, other)
# object.__xor__(self, other)
# object.__or__(self, other)
# These methods are called to implement the binary arithmetic operations (+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |). For instance, to evaluate the expression x + y, where x is an instance of a class that has an __add__() method, x.__add__(y) is called. The __divmod__() method should be the equivalent to using __floordiv__() and __mod__(); it should not be related to __truediv__(). Note that __pow__() should be defined to accept an optional third argument if the ternary version of the built-in pow() function is to be supported.

# If one of those methods does not support the operation with the supplied arguments, it should return NotImplemented.

# object.__radd__(self, other)
# object.__rsub__(self, other)
# object.__rmul__(self, other)
# object.__rmatmul__(self, other)
# object.__rtruediv__(self, other)
# object.__rfloordiv__(self, other)
# object.__rmod__(self, other)
# object.__rdivmod__(self, other)
# object.__rpow__(self, other[, modulo])
# object.__rlshift__(self, other)
# object.__rrshift__(self, other)
# object.__rand__(self, other)
# object.__rxor__(self, other)
# object.__ror__(self, other)
# These methods are called to implement the binary arithmetic operations (+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |) with reflected (swapped) operands. These functions are only called if the left operand does not support the corresponding operation 3 and the operands are of different types. 4 For instance, to evaluate the expression x - y, where y is an instance of a class that has an __rsub__() method, y.__rsub__(x) is called if x.__sub__(y) returns NotImplemented.

# Note that ternary pow() will not try calling __rpow__() (the coercion rules would become too complicated).

# Note If the right operand’s type is a subclass of the left operand’s type and that subclass provides a different implementation of the reflected method for the operation, this method will be called before the left operand’s non-reflected method. This behavior allows subclasses to override their ancestors’ operations.
# object.__iadd__(self, other)
# object.__isub__(self, other)
# object.__imul__(self, other)
# object.__imatmul__(self, other)
# object.__itruediv__(self, other)
# object.__ifloordiv__(self, other)
# object.__imod__(self, other)
# object.__ipow__(self, other[, modulo])
# object.__ilshift__(self, other)
# object.__irshift__(self, other)
# object.__iand__(self, other)
# object.__ixor__(self, other)
# object.__ior__(self, other)
# These methods are called to implement the augmented arithmetic assignments (+=, -=, *=, @=, /=, //=, %=, **=, <<=, >>=, &=, ^=, |=). These methods should attempt to do the operation in-place (modifying self) and return the result (which could be, but does not have to be, self). If a specific method is not defined, the augmented assignment falls back to the normal methods. For instance, if x is an instance of a class with an __iadd__() method, x += y is equivalent to x = x.__iadd__(y) . Otherwise, x.__add__(y) and y.__radd__(x) are considered, as with the evaluation of x + y. In certain situations, augmented assignment can result in unexpected errors (see Why does a_tuple[i] += [‘item’] raise an exception when the addition works?), but this behavior is in fact part of the data model.

# object.__neg__(self)
# object.__pos__(self)
# object.__abs__(self)
# object.__invert__(self)
# Called to implement the unary arithmetic operations (-, +, abs() and ~).

# object.__complex__(self)
# object.__int__(self)
# object.__float__(self)
# Called to implement the built-in functions complex(), int() and float(). Should return a value of the appropriate type.

# object.__index__(self)
# Called to implement operator.index(), and whenever Python needs to losslessly convert the numeric object to an integer object (such as in slicing, or in the built-in bin(), hex() and oct() functions). Presence of this method indicates that the numeric object is an integer type. Must return an integer.

# If __int__(), __float__() and __complex__() are not defined then corresponding built-in functions int(), float() and complex() fall back to __index__().

# object.__round__(self[, ndigits])
# object.__trunc__(self)
# object.__floor__(self)
# object.__ceil__(self)
# Called to implement the built-in function round() and math functions trunc(), floor() and ceil(). Unless ndigits is passed to __round__() all these methods should return the value of the object truncated to an Integral (typically an int).

# The built-in function int() falls back to __trunc__() if neither __int__() nor __index__() is defined.

# review datetime.py library