# utils.py
from functools import wraps
import gc
import timeit


def measure_time(f, no_print=False, disable_gc=False):
    """
    decorator to measure time execution
    :param f: the function for which time execution will be measured
    :param no_print:
    :param disable_gc:
    :return:
    """
    @wraps(f)
    def _wrapper(*args, **kwargs):
        gcold = gc.isenabled()
        if disable_gc:
            gc.disable()
        start_time = timeit.default_timer()
        try:
            result = f(*args, **kwargs)
        finally:
            elapsed = timeit.default_timer() - start_time
            if disable_gc and gcold:
                gc.enable()
            if not no_print:
                print('execution time measured for function "{}": {}s'.format(f.__name__, elapsed))
        return result
    return _wrapper


class MeasureBlockTime:
    def __init__(self,name="(block)", no_print=False, disable_gc=False):
        self.name = name
        self.no_print = no_print
        self.disable_gc = disable_gc

    def __enter__(self):
        self.gcold = gc.isenabled()
        if self.disable_gc:
            gc.disable()
        self.start_time = timeit.default_timer()

    def __exit__(self,ty,val,tb):
        self.elapsed = timeit.default_timer() - self.start_time
        if self.disable_gc and self.gcold:
            gc.enable()
        if not self.no_print:
            print('Function "{}": {}s'.format(self.name, self.elapsed))
        return False  # re-raise any exceptions


minutesInDay = 60 * 24


def minuteToString(time):
    hour = str(int(time / 60))
    minute = str(int(time % 60))

    if len(hour) == 1:
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute

    return hour + ':' + minute


def stringToMinute(time):
    if not isinstance(time, str):
        raise TypeError(f"string type expected not {type(time)}")
    hour, minute = time.split(':')
    return 60 * int(hour) + int(minute)