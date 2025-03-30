from functools import wraps


def cache(func):
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (func, args, tuple(kwargs.items()))

        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cached_results[key] = result
        return result

    return wrapper

