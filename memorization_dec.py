def memorization_dec(func):
    cache = {}

    def wrapper(*args, **kwargs):
        k = (args, tuple(kwargs.keys()))
        if k not in cache:
            # print(k)
            cache[k] = func(*args, **kwargs)
            # print(cache)
        return cache[k]
    print(cache)
    return wrapper


@memorization_dec
def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))
print(fact(4))
