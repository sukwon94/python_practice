#. def(definition of function)
#. def doesn't run a code we have to invoke(call)

def SW():
    print('def can store a function')
    print('and reuse')
SW()

#. def can remember function only
#. and this is how to return a string
def greet():
    return "this is return value 'hello'"
print(greet(), ", name")

#def can get 2 or more parameters

def addtwo(a,b):
    added=a+b
    return added
x=addtwo(3,5)
print(x)

#python already have some def functions like max, min
a=max('Hello world')
b=min('Hello world')
print(a)
print(b)
#lower case is bigger than upper case, 'space'is smallest
