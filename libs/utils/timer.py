import time

def timer_func(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executado em {end_time - start_time:.2f} segundos")
        return result
    return wrapper