class List(object):

    '''
       Explain how to implement growing factor :

       We set the initial capacity and initial size when initializing the class.

       When the content added by the dynamic linked list reaches the set capacity,

       it will be expanded twice and the size will be re-assigned.

       Just like in line 71, if the element is full after adding, call the _resize function to expand the capacity,

       where 2 is the set growth factor.

       '''

    def __init__(self,capacity=10):
        self._capacity = capacity
        self._size = 0  # 数组有效元素的数目，初始化为0
        self._data = [None] * self._capacity
        self.start = 0

    def size(self):
        return self._size

    def _resize(self,new_capacity):
        new_arr = List(new_capacity)
        for i in range(self._size):
            new_arr.add_to_tail(self._data[i])
        self._capacity = new_capacity
        self._data = new_arr._data

    def get_capacity(self):
        return self._capacity

    def find(self, elem):
        for i in range(self._size):  # 遍历数组
            if self._data[i] == elem:
                return i  # 找到就返回索引
        return -1

    def remove(self, index):

        if index < 0 or index >= self._size:
            raise Exception('Remove failed.Require 0 <= index < self._size')

        ret = self._data[index]

        for i in range(index + 1, self._size):
            self._data[i - 1] = self._data[i]

        self._size -= 1
        self._data[self._size] = None

        if self._size and self._capacity // self._size == 4:
            self._resize(self._capacity // 2)
        return ret

    def remove_element(self, elem):

        index = self.find(elem)
        if index != -1:
            self.remove(index)


    def is_empty(self):
        return  self._size == 0

    def add(self, index, elem):
        if index < 0 or index > self._size:
            raise Exception('Add Filed.')

        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        for i in range(self._size - 1, index - 1, -1):
            self._data[i + 1] = self._data[i]

        self._data[index] = elem
        self._size += 1

    def add_to_tail(self, elem):
        self.add(self._size, elem)
    # def from_list(self,):

    def add_to_head(self, elem):
        self.add(0, elem)

    def to_list(self):
        res = []
        for i in range(self._size):
            res.append(self._data[i])
        return  res

    def from_list(self,lft):
        if len(lft)==0:
            return self
        else:
            for i in lft:
                self.add_to_tail(i)

    def _last_node(self):
        return self.lt[self.size()-1]


    def str(self):
        for i in range(self.size()):
            print(self._data[i])

    def map(self,f):
        for i in range(self.size()):
            cur = self._data[i]
            self._data[i] = f(cur)

    def reduce(self,f,initial_state):
        state = initial_state
        for i in range(self.size()):
            cur = self._data[i]
            state = f(state,cur)
        return state

    def findAll(self, elem):
        a = []
        for i in range(self._size):  # 遍历数组
            if self._data[i] == elem:
                a.append(i)

        return a



    # def mempty(self):
    #     return None
    #
    # def mconcat(self, b):
    #     if self.isEmpty()==True:
    #         return b
    #     tmp = self.reverse()
    #     res = b
    #     for i in range(len(tmp)):
    #         res = self.add( 0, tmp[i])
    #     return res


    def __iter__(self):
        return self

    def __next__(self):
        if self._size == self.size():
           raise StopIteration
        self.start = self.start + 1
        tmp = self._data[self.start]
        return tmp









