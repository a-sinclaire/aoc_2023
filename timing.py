# Amelia Sinclaire
import time
import numpy as np


class SwitchedDecorator:
    def __init__(self, enabled_func):
        self._enabled = True
        self._enabled_func = enabled_func

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, new_value):
        if not isinstance(new_value, bool):
            raise ValueError("enabled can only be set to a boolean value")
        self._enabled = new_value

    def __call__(self, target):
        if self._enabled:
            return self._enabled_func(target)
        return target


def time_it_decorator_function(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        returned_value = func(*args, **kwargs)
        times = [time.time() - start]
        while sum(times) < 0.02:
            start = time.time()
            returned_value = func(*args, **kwargs)
            times.append(time.time()-start)
        print(f'{func.__name__} takes {np.average(times)}s on average over {len(times)} iterations.')
        return returned_value
    return wrapper


time_it_decorator = SwitchedDecorator(time_it_decorator_function)
