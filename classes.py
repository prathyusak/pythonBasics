##################
#Class 
#Each value is an object, and therefore has a class (also called its type). It is stored as object.__class__.
#Class objects support two kinds of operations: attribute references and instantiation
#Attribute references =>MyClass.i,MyClass.f
#Instantiation => x =MyClass() (automatically invokes __init__ if exists )

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
#C struct or Pascal record with empty cls
class Employee:
    pass
john = Employee()  # Create an empty employee record
# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

######################
#Instance Objects  => Data attributes , method

x = MyClass()
x.counter = 1   # Data attributes need not be declared; like local variables, 
                # they spring into existence when they are first assigned to.
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
print(x.i)
x.j =2
print(x.j)
####################
#Method Objects
xf= x.f
xf()    #equals MyClass.f(x)

#here f,g,h are all methods of instances of C
def f1(self, x, y):
    return min(x, x+y)
class C:
    f = f1
    def g(self):
        return 'hello world'
    h = g
#Methods can call other methods
class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)

###################
#class and Instance variables
class Dog:
    kind = 'canine'         # class variable shared by all instances
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
d = Dog('Fido')
e = Dog('Buddy')
d.age =7 #instacne variable
d.kind   #shared by all dogs

class Dog:
    tricks = []             # mistaken use of a class variable
    def __init__(self, name):
        self.name = name
        self.Tricks = []    #creates new empty list for each dog
    def add_trick(self, trick):
        self.tricks.append(trick)
        self.Tricks.append(trick) 
d = Dog('Fido') 
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)         #['roll over', 'play dead']
print(e.tricks)         #['roll over', 'play dead']
print(d.Tricks)         #['roll over']
print(e.Tricks)         #['play dead']
####################
#Inheritance
class X:pass
class Y:pass
class Z:pass
class A(X,Y):pass 
class B(Y,Z):pass
class M(B,A,Z):pass
x=1
isinstance(x, int) # True
issubclass(bool, int) #True
print(issubclass(A,X)) #True
print(isinstance(d,Dog))  #True

##########################
#Polymorphism
class A:
    def explore(self):
        print("explore() method from class A")
class B(A):
    def explore(self):
        super(B, self).explore()   #A.explore(self)    #super().explore()
        print("explore() method from class B")
def poly_mor(char):
    char.explore()
a_obj=A()
b_obj=B()
#poly_mor(a_obj)
#poly_mor(b_obj)
for char in [a_obj,b_obj]:
    poly_mor(char)
####################
#Private Variables  (_spam is treated as nonpublic variable)
#Name mangling __spam =>_className__spam (subclasses override methods without breaking 
                                         # intraclass method calls)
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

####################
#Scopes and Namespace

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)     #test spam
    do_nonlocal()
    print("After nonlocal assignment:", spam)   #nonlocal spam
    do_global()
    print("After global assignment:", spam)     #nonlocal spam

scope_test()
print("In global scope:", spam)             #global spam