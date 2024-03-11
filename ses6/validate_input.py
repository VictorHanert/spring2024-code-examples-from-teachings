def validate_inputs(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("All arguments must be integers")
        for value in kwargs.values():
            if not isinstance(value, int):
                raise TypeError("All keyword arguments must be integers")
        return func(*args, **kwargs)
    return wrapper


@validate_inputs
def listOfStuff(*args):
    return args