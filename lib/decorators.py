from datetime import datetime

def timing(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f"{func.__name__} time: {end - start}s")
        return result
    return wrapper
