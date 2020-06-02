from ctypes import py_object
def size(n):
    s = 0
    for e in n:
        if e is not None:
            s += 1
    return s

def remove(arr, index):
    if index < 0 or index > len(arr):
        return False
    arr = list(arr)
    for i in range(index + 1, len(arr)):
        arr[i - 1] = arr[i]
    del arr[len(arr)-1]
    return arr

#growth factor
def make_array(a):
    return (a * py_object)()
def resize_lenth(arr, length):
    New = make_array(length)
    for i in range(len(arr)):
        New[i] = arr[i]
    return len(New)

def insert(arr, index, n):
    if size(arr) == len(arr):
        resize_lenth(arr, len(arr))
    if index < 0:
        index = len(arr) + index + 1
    tmp_arr = arr[:index] + [n] + arr[index:]
    return tmp_arr

def from_list(arr):
    res = []
    for e in arr:
        res.append(e)
    return res

def to_list(n):
    if n is None:
        return []
    res = []
    cur = n
    for i in range(len(n)):
        if cur[i] is not None:
            res.append(cur[i])
    return res

def find(arr, n):
    index = 0
    idx_list = []
    for v in arr:
        if v == n:
            idx_list.append(index)
        index += 1
    if len(idx_list) == 0:
        return None
    elif len(idx_list) == 1:
        return idx_list[0]
    else:
        return idx_list

def filter(arr, filt):
    tmp_arr = []
    for v in arr:
        if v != filt:
            tmp_arr.append(v)
    return tmp_arr

def map(arr, f):
    i = 0
    tmp_arr = arr.copy()
    for v in arr:
        tmp_arr[i] = f(v)
        i += 1
    return tmp_arr

def reduce(arr, f, initial_state):
    state = initial_state
    for v in arr:
        state = f(state, v)
    return state

def reverse(arr):
    arr = arr[::-1]
    return arr

def mempty():
    return list([])

def mconcat(a, b):
    tmp_arr = a + b
    return tmp_arr
def iterator(arr):
    idx = 0
    def foo():
        nonlocal idx, arr
        len_arr = len(arr)
        if idx >= len_arr: raise StopIteration
        value = arr[idx]
        idx += 1
        return value
    return foo