import unittest
from hypothesis import given
import hypothesis.strategies as st
from mutable import *
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
        list.remove_element('a')
        self.assertEqual(list.to_list(),['b','c'] )
        list.remove_element('b')
        self.assertEqual(list.to_list(),['c'])
        list.remove_element('c')
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

    def test_growing(self):
        list = List()
        list.add_to_tail('a')
        list.add_to_tail('b')
        list.add_to_tail('c')
        list.add_to_tail('d')
        list.add_to_tail('e')
        self.assertEqual(list._capacity, 5)
        list.add_to_tail('f')
        self.assertEqual(list._capacity, 10)




    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        lst = List()
        lst.from_list(a)
        b = lst.to_list()
        self.assertEqual(a, b)


    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        lst = List()
        lst.from_list(a)
        self.assertEqual(lst.size(), len(a))

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        l = List()
        self.assertEqual(l.mconcat(l.mempty(), lst), lst)
        self.assertEqual(l.mconcat(lst, l.mempty()), lst)

    @given(st.lists(st.integers()), st.lists(st.integers()), st.lists(st.integers()))
    def test_monoid_associativity(self, lst1, lst2, lst3):
        l1 = List()
        self.assertEqual(l1.mconcat(l1.mempty(), lst1), lst1)
        l2 = List()
        self.assertEqual(l2.mconcat(l2.mempty(), lst1), l2.mconcat(lst1, l2.mempty()))
        l3 = List()
        self.assertEqual(l3.mconcat(l3.mconcat(lst1, lst2), lst3), l3.mconcat(lst1, l3.mconcat(lst2, lst3)))




    def test_iter(self):
        x = [1, 2, 3]
        lst = List()
        lst.from_list(x)
        i = iter(lst)
        self.assertRaises(StopIteration, lambda: next(i))


if __name__ == '__main__':
    unittest.main()