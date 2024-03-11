import datetime

def log_decorator(func):
    def wrapper(*args):
        currentTime = datetime.datetime.now()
        # Write to log file:
        f = open('log.txt', 'a')
        f.write(f"{currentTime} - Function \"{func.__name__}\" called with args: {args}\n")
        f.write(f"{currentTime} - Result: {func(*args)}\n")
        return "Result logged to log.txt: ", func(*args)
    return wrapper

# Decorate the add function with the log decorator
@log_decorator # is the same as: "add = log_decorator(add)"
def add(*args):
    return sum(args)

# Testing the add function
print(add(1, 2, 3)) # Output will be 6, and logs will be written to log.txt
