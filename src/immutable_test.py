import unittest
from hypothesis import given
import hypothesis.strategies as st
from immutable import *
class TestImmutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(size([]), 0)
        self.assertEqual(size([1]), 1)
        self.assertEqual(size([1, 2]), 2)
    def test_remove(self):
        self.assertEqual(remove([1, 2, 3], 0), [2, 3])
        self.assertEqual(remove([1, 2, 3], 1), [1, 3])
        self.assertEqual(remove([1, 2, 3], 2), [1, 2])
    def test_insert(self):
        self.assertEqual(insert([1, 3], 1, 2), [1, 2, 3])
        self.assertEqual(insert([1, 3], 2, 2), [1, 3, 2])
        self.assertEqual(insert([1, 3], 0, 2), [2, 1, 3])
    def test_from_list(self):
        test_data = [
            [],
            [1],
            [1, 2]
        ]
        for e in test_data:
            self.assertEqual(to_list(from_list(e)), e)
    def test_to_list(self):
        self.assertEqual(to_list(None), [])
        self.assertEqual(to_list([1, None]), [1])
        self.assertEqual(to_list([1, 2, None]), [1, 2])
    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        self.assertEqual(to_list(from_list(a)), a)
    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        a = from_list(lst)
        self.assertEqual(mconcat(mempty(), a), a)
        self.assertEqual(mconcat(a, mempty()), a)
    @given(st.lists(st.integers()), st.lists(st.integers()), st.lists(st.integers()))
    def test_monoid_associativity(self, lst1, lst2, lst3):
        a = from_list(lst1)
        b = from_list(lst2)
        c = from_list(lst3)
        self.assertEqual(mconcat(mempty(), a), a)
        self.assertEqual(mconcat(mempty(), a), mconcat(a, mempty()))
        self.assertEqual(mconcat(mconcat(a, b), c), mconcat(a, mconcat(b, c)))
    def test_find(self):
        self.assertEqual(find([], 1), None)
        self.assertEqual(find([1, 2, 3], 1), 0)
        self.assertEqual(find([1, 2, 3], 2), 1)
    def test_filter(self):
        self.assertEqual(filter([0, 1, 2], 1), [0, 2])
        self.assertEqual(filter([0, 1, 2], 2), [0, 1])
    def test_map(self):
        self.assertEqual(map([], str), [])
        self.assertEqual(map([1, 2, 3, 4], str), ['1', '2', '3', '4'])
    def test_reduce(self):
        self.assertEqual(reduce([], lambda st, e: st + e, 0), 0)
        self.assertEqual(reduce([1, 2, 3, 4], lambda st, _: st + 1, 0), 4)
    def test_reverse(self):
        self.assertEqual(reverse([1, 2]), [2, 1])
        self.assertEqual(reverse([1, 2, 3]), [3, 2, 1])
    def test_mconcat(self):
        self.assertEqual(mconcat([], []), [])
        self.assertEqual(mconcat([], [1, 2]), [1, 2])
        self.assertEqual(mconcat([1, 2], [3, 4]), [1, 2, 3, 4])
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