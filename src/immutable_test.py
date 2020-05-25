import unittest
from hypothesis import given
import hypothesis.strategies as st
from immutable import *
class TestImmutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(size(None), 0)
        self.assertEqual(size(['a']), 1)
        self.assertEqual(size(['a', 'b']), 2)
    def test_remove(self):
        self.assertEqual(remove(['a', 'b', 'c'], 0), ['b', 'c'])
        self.assertEqual(remove(['a', 'b', 'c'], 1), ['a', 'c'])
        self.assertEqual(remove(['a', 'b', 'c'], 2), ['a', 'b'])
    def test_add(self):
        self.assertEqual(add(['a', 'c'], 1, 'b'), ['a', 'b', 'c'])
        self.assertEqual(add(['a', 'c'], 2, 'b'), ['a', 'c', 'b'])
        self.assertEqual(add(['a', 'c'], 0, 'b'), ['b', 'a', 'c'])
    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            self.assertEqual(to_list(from_list(e)), e)
    def test_to_list(self):
        self.assertEqual(to_list(None), [])
        self.assertEqual(to_list(['a', None]), ['a'])
        self.assertEqual(to_list(['a', 'b', None]), ['a', 'b'])
    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        self.assertEqual(to_list(from_list(a)), a)
    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        a = from_list(lst)
        self.assertEqual(mconcat(mempty(), a), a)
        self.assertEqual(mconcat(a, mempty()), a)
    @given(st.lists(st.integers()))
    def test_monoid_associativity(self, lst):
        a = from_list(lst)
        b = from_list(lst)
        c = from_list(lst)
        self.assertEqual(mconcat(mempty(), a), a)
        self.assertEqual(mconcat(mempty(), a), mconcat(a, mempty()))
        self.assertEqual(mconcat(mconcat(a, b), c), mconcat(a, mconcat(b, c)))
    def test_find(self):
        self.assertEqual(find(None, 'a'), False)
        self.assertEqual(find(['a', 'b', 'c'], 'a'), 0)
        self.assertEqual(find(['a', 'b', 'c'], 'b'), 1)
    def test_filter(self):
        self.assertEqual(filter(['a', 1, 'c'], int), ['a', 'c'])
        self.assertEqual(filter(['a', 1, 'c'], str), [1])
    def test_map(self):
        self.assertEqual(map([], str), [])
        self.assertEqual(map([1, 2, 3, 4], str), ['1', '2', '3', '4'])
    def test_reduce(self):
        self.assertEqual(reduce([], lambda st, e: st + e, 0), 0)
        self.assertEqual(reduce([1, 2, 3, 4], lambda st, _: st + 1, 0), 4)
    def test_reverse(self):
        self.assertEqual(reverse(['a', 'b']), ['b', 'a'])
        self.assertEqual(reverse(['a', 'b', 'c']), ['c', 'b', 'a'])
    def test_mconcat(self):
        self.assertEqual(mconcat(['a', 'b'], 'c'), ['a', 'b', 'c'])
        self.assertEqual(mconcat(['a', 'b'], ['c', 'd']), ['a', 'b', 'c', 'd'])
    def test_iter(self):
        arr = [1, 2, 3]
        tmp = []
        try:
            get_next = iterator(arr)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(arr, tmp)
    def test_resize_lenth(self):
        arr = [1, 2, 3]
        self.assertEqual(resize_lenth(arr, 6), 6)
        arr = [1]
        self.assertEqual(resize_lenth(arr, 2), 2)

if __name__ == '__main__':
    unittest.main()