def validation_dec(original_func):
    def wrapper(*args, **kwargs):
        k = args + tuple(kwargs.values())
        for i in k:
            if not isinstance(i, int):
                raise ValueError(f"{i} must be integer")
            if i < 0 or i > 10000:
                raise ValueError(f"{i} must be between 0 and 10 but got {i}")
        return original_func(*args, **kwargs)
    return wrapper


@validation_dec
def mul(a, b, c, d):
    return a * b * c * d


try:
    print(mul(4, 5, 6, 7))
except ValueError as ve:
    print(str(ve))