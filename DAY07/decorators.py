def decorator(r):
    def wrapper():
        print("About to run the function")
        r()
        print("Run the function successfully")
    return wrapper


@decorator
def f():
    print("Hello world")


f()
