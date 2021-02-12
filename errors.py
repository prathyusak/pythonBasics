#Syntax Errors and Exceptions
#while True print('Hello world') => syntax error
#ZeroDivisionError =>10 * (1/0)
#NameError => 4 + spam*3
#TypeError =>  '2' + 2
#################
# Handling Exceptions
import sys
def this_fails():
    x = 1/0
while True:
    try:
        x = int(input("Please enter a number: "))
        this_fails()
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except (RuntimeError, TypeError, NameError):   #except clause can have multiple exceptions
        pass
    except ZeroDivisionError as err:  
        print('Handling run-time error:', err)
        break
    except:   #empty exception name serves as wildcard
        print("Unexpected error:", sys.exc_info()[0])
        raise    #raising exceptions
################
#Exception chaining : when exception raised from except or finally block

# try:
#     open('database.sqlite')
# except IOError as ioerr :
#     raise RuntimeError from ioerr

# #To disable exception chaining
# try:
#     open('database.sqlite')
# except IOError as ioerr :
#     raise RuntimeError from None
 

################
#try except else finally 

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:     #additional code in try block
        print("result is", result)
    finally:   # executes at all times , cleanup acions
        print("executing finally clause")


################
#User defined exceptions
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
#####################
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]: 
    try:
        raise cls()
    except B:
        print("B")
        # raise InputError('erro','mess')
    except D:   #an except clause listing a derived class is not compatible with a base class
        print("D")
    except C:
        print("C")
