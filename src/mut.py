import unittest
from hypothesis import given
import hypothesis.strategies as st
from p1 import *
class TestMutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(List().size(), 0)
        lt = List()
        lt.add_to_tail('a')
        self.assertEqual(lt.size(), 1)
        lt.add_to_tail('b')
        self.assertEqual(lt.size(), 2)

    def test_remove(self):
        list = List()
        list.add_to_tail('a')
        list.add_to_tail('b')
        list.add_to_tail('c')
        list.removeElement('a')
        self.assertEqual(list.to_list(),['b','c'] )
        list.removeElement('b')
        self.assertEqual(list.to_list(),['c'])
        list.removeElement('c')
        self.assertEqual(list.to_list(), [])

    def test_to_list(self):
        self.assertEqual(List().to_list(), [])
        lt = List()
        lt.add_to_tail('a')
        self.assertEqual(lt.to_list(), ['a'])
        lt.add_to_tail('b')
        self.assertEqual(lt.to_list(), ['a', 'b'])

    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        
        for e in test_data:
            lst = List()
            lst.from_list(e)
            self.assertEqual(lst.to_list(), e)
    def test_add_to_head(self):
        lst = List()
        self.assertEqual(lst.to_list(), [])
        lst.add_to_head('a')
        self.assertEqual(lst.to_list(), ['a'])
        lst.add_to_head('b')
        self.assertEqual(lst.to_list(), ['b', 'a'])

    def test_add_to_tail(self):
        lst = List()
        self.assertEqual(lst.to_list(), [])
        lst.add_to_tail('a')
        self.assertEqual(lst.to_list(), ['a'])
        lst.add_to_tail('b')
        self.assertEqual(lst.to_list(), ['a', 'b'])

    def test_map(self):
        lst = List()
        lst.map(str)
        self.assertEqual(lst.to_list(), [])
        lst = List()
        lst.from_list([1, 2, 3])
        lst.map(str)
        self.assertEqual(lst.to_list(), ["1", "2", "3"])

    def test_reduce(self):  # sum of empty list
        lst = List()
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 0)
        # sum of list
        lst = List()
        lst.from_list([1, 2, 3])
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 6)        # size
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            lst = List()
            lst.from_list(e)
            self.assertEqual(lst.reduce(lambda st, _: st + 1, 0), lst.size())
    def test_findall(self):
        list = List()
        list.add_to_tail('a')
        list.add_to_tail('b')
        list.add_to_tail('c')
        list.add_to_tail('b')
        self.assertEqual(list.findAll('b'),[1,3] )


    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        lst = List()
        lst.from_list(a)
        self.assertEqual(lst.size(), len(a))
    #
    # def test_mconcat(self):
    #     lst = List(['a', 'b'])
    #     self.assertEqual(lst.mconcat('c'), ['a', 'b', 'c'])
    #     lst = List(['a', 'b'])
    #     self.assertEqual(lst.mconcat(['c', 'd']), ['a', 'b', 'c', 'd'])
    # @given(st.lists(st.integers()))
    #
    # def test_monoid_identity(self, lst):
    #     lst = List()
    #     a = lst.from_list(lst)
    #     self.assertEqual(a.mconcat([]), )
    #     self.assertEqual(mconcat(a, []), a)

    def test_iter(self):
        x = [1, 2, 3]
        lst = List()
        lst.from_list(x)
        i = iter(lst)
        self.assertRaises(StopIteration, lambda: next(i))


if __name__ == '__main__':
    unittest.main()