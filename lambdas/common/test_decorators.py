# Testing decorators

def decorator(func):
    print('Runs during compilation')
    def wrapper():
        print('Starting')
        func()
        print('Ended')

    return wrapper

@decorator
def func():
    print('Hello')


# Create a dictionary

