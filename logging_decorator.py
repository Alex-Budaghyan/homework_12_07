def logging_dec(original_func):
    import logging
    logging.basicConfig(filename=f"{original_func.__name__}.log", level=logging.INFO)
    print(original_func.__name__)

    def wrapper(*args, **kwargs):
        logging.info(f"Function: {original_func.__name__}")
        logging.info(f"Input arguments: {args} and {kwargs}")
        return original_func(*args, **kwargs)

    return wrapper


@logging_dec
def mul(m, n):
    return m * n


mul(4, 5)