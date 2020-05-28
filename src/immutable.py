from ctypes import py_object
def size(n):
    if n is None:
        return 0
    else:
        return len(n)

def remove(arr, index):
    if index < 0 or index > len(arr):
        return False
    arr = list(arr)
    for i in range(index + 1, len(arr)):
        arr[i - 1] = arr[i]
    del arr[len(arr)-1]
    return arr

def add(arr, index, n):
    # here, if the array is full, it enlarges growth factor times automatically.It realize the purpose of dynamic array
    if size(arr) == len(arr):
        resize_lenth(arr, len(arr))
    if index < 0 or index > len(arr):
        return False
    arr = list(arr)
    if arr is None:
        return n
    else:
        arr.insert(index, n)
    return arr

def from_list(arr):
    res = []
    # for e in reversed(lst):
    for e in arr:
        # res = add(e, 0, res)
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
    if arr is None:
        return False
    arr = list(arr)
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return False

def filter(arr, filt):
    res = []
    for i in range(len(arr)):
        if type(arr[i]) != filt:
            res.append(arr[i])
    return res

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
    return None

def mconcat(a, b):
    if a is None:
        return b
    if b is None:
        return a
    tmp = reverse(a)
    res = b
    for i in range(len(tmp)):
            res = add(res, 0, tmp[i])
    return res

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

#growth factor
# I rebulid a arrry which is 2 times of lst, then set the value of lst to the new array(New), finally, let lst equal New
def make_array(a):
    return (a * py_object)()
def resize_lenth(arr, length):
    New = make_array(length)
    for i in range(len(arr)):
        New[i] = arr[i]
    return len(New)