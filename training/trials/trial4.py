# returning a function
def hello(name='Fraize'):
    print('the hello() func has been run')

    def greet():
        return "    This is inside greet()"

    def welcome():
        return "    this is inside welcome()"

    if name =="Fraize":
        return greet
    else:
        return welcome

x = hello(name= 'sam')
print(x())

# return a function2 ---- passing functionn as an arg
def hello():
    return "Hi Fraiser"

def other(func):
    print("some other code")
    print(func())

other(hello)

# decorators
def new_decorator(func):
    def wrap_func():
        print("some code before executing func")

        func()

        print("code here")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("Please decorate me!!!")

func_needs_decorator()
