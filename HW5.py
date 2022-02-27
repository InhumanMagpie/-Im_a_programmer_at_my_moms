from datetime import datetime
from functools import reduce

mylist = [[1, 4, 6, 5, 3], [4, 3, 6, 9], [9, 7, 4, 6, 2]]


def decorator(func):
    def wrapper(*args, **kwargs):
        print(f'{datetime.now()} | Start {func.__name__}')
        result = func(*args, **kwargs)
        print(f'{datetime.now()} | Stop {func.__name__}')
        return result

    return wrapper


@decorator
def list_concatener(lst) -> list:
    """Concatenates all lists within a list"""
    list_concatenated = reduce(lambda x, y: x + y, lst)
    return list_concatenated


my_newlst = list_concatener(mylist)
print(my_newlst)
