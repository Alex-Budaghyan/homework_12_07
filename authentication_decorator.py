class LoggedError(Exception):
    pass

def user_is_logged_in():
    pass


def authentication_dec(original_func):
    def wrapper(*args, **kwargs):
        if not user_is_logged_in():
            raise Exception("User is not logged")
        return original_func(*args, **kwargs)

    return wrapper


@authentication_dec
def foo():
    print('This func')


try:
    foo()
except LoggedError as le:
    print(str(le))