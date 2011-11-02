from pandas import *

import numpy as np
from itertools import izip
from pandas.util.testing import rands
import pandas._tseries as lib

N = 100000

key1 = [rands(10) for _ in xrange(N)]
key2 = [rands(10) for _ in xrange(N)]

zipped = izip(key1, key2)

def _zip(*args):
    arr = np.empty(N, dtype=object)
    arr[:] = zip(*args)
    return arr

def _zip2(*args):
    return lib.list_to_object_array(zip(*args))

index = MultiIndex.from_arrays([key1, key2])
to_join = DataFrame({'j1' : np.random.randn(100000)}, index=index)

data = DataFrame({'A' : np.random.randn(500000),
                  'key1' : np.repeat(key1, 5),
                  'key2' : np.repeat(key2, 5)})

# data.join(to_join, on=['key1', 'key2'])

"""
Cython function for list_to_object_array

def list_to_object_array(list obj):
    '''
    Convert list to object ndarray. Seriously can't believe I had to write this
    function
    '''
    cdef:
        Py_ssize_t i, n
        ndarray[object] arr

    n = len(obj)
    arr = np.empty(n, dtype=object)

    for i from 0 <= i < n:
        arr[i] = obj[i]

    return arr
"""



