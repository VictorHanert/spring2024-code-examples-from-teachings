import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

# Testing:
@time_it
def example_function(n):
    # Simulating some time-consuming computation
    total = 0
    for i in range(n):
        total += i
    return total

print("testing... ", example_function(1000000))
