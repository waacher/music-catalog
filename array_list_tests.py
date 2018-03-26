# Tests for array list implementation

import unittest
from array_list import *

# function to test sort
# determines if the title attribute of one object is smaller than the other
def less_than(x, y):
    if x.title < y.title:
        return True
    return False

# function to test foreach
# increments the inputted value by one
def foreach_test_func(x):
    return x + 1

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)
    def test_eq(self):
        self.assertEqual(List([1, None], 1, 2), List([1, None], 1, 2))
    def test_repr(self):
        self.assertEqual(repr(List([1, 2, 3, None], 3, 4)), "List({!r}, {!r}, {!r})".format([1, 2, 3, None], 3, 4))
    def test_empty_list(self):
        self.assertEqual(empty_list(), List([None], 0, 1))
    def test_add_empty_valid(self):
        self.assertEqual(add(List([None], 0, 1), 0, 1), List([1], 1, 1))
    def test_add_empty_invalid(self):
        self.assertRaises(IndexError, add, List([None, None], 0, 2), 1, 4)
    def test_add_valid_double(self):
        self.assertEqual(add(List([1, 2, 3, 5], 4, 4), 3, 4), List([1, 2, 3, 4, 5, None, None, None], 5, 8))
    def test_add_neg_index(self):
        self.assertRaises(IndexError, add, List([1, 2], 2, 2), -5, 15)
    def test_add_valid_cap(self):
        self.assertEqual(add(List([1, 2, 3, None], 3, 4), 3, 4), List([1, 2, 3, 4], 4, 4))
    def test_add_valid_mid(self):
        self.assertEqual(add(List([1, 3, 4, None], 3, 4), 1, 2), List([1, 2, 3, 4], 4, 4))
    def test_length_empty(self):
        self.assertEqual(length(List([None], 0, 1)), 0) 
    def test_length_small(self):
        self.assertEqual(length(List([1, 2, 3, 4, 5], 5, 5)), 5)
    def test_get_empty(self):
        self.assertRaises(IndexError, get, List([None], 0, 1), 3)
    def test_get_neg_index(self):
        self.assertRaises(IndexError, get, List([1, None], 1, 2), -3)
    def test_get_valid(self):
        self.assertEqual(get(List([1, 2, 3, None], 3, 4), 1), 2)    
    def test_set_empty_valid(self):
        self.assertRaises(IndexError, set, List([None], 0, 1), 0, 34)
    def test_set_neg_index(self):
        self.assertRaises(IndexError, set, List([1, 2, 3], 3, 4), -3, 3)
    def test_set_empty_error(self):
        self.assertRaises(IndexError, set, List([None], 0, 1), 34, 16)
    def test_set_mid(self):
        self.assertEqual(set(List([1, 2, 3, 5, 6], 5, 8), 3, 4), List([1, 2, 3, 4, 6], 5, 8))
    def test_remove_empty(self):
        self.assertRaises(IndexError, remove, List([None], 0, 1), 2)
    def test_remove_neg_index(self):
        self.assertRaises(IndexError, remove, List([1, 2, 3, None], 3, 4), -31)
    def test_remove_valid(self):
        self.assertEqual(remove(List([1, 3, 5, None], 3, 4), 2), (5, List([1, 3, None, None], 2, 4)))
    def test_remove_valid_2(self):
        self.assertEqual(remove(List([1, None, None, None], 1, 4), 0), (1, List([None, None, None, None], 0, 4)))
    def test_remove_valid_3(self):
        self.assertEqual(remove(List([1, 2, 3, None], 3, 4), 1), (2, List([1, 3, None, None], 2, 4)))
    
    def test_repr_song(self):
        self.assertEqual(repr(Song('title', 'artist', 'album', 'num')), "Song('title', 'artist', 'album', 'num')")
    def test_search_mid(self):
        self.assertEqual(search(List([Song('ok', 'ok', 'ok', '4'), Song('asd', 'qwe', 'zxc', '1'), Song('hi', 'hi', 'hi', '15'), None], 3, 4), 1), Song('asd', 'qwe', 'zxc', '1'))

    def test_foreach_empty(self):
        lst = empty_list()
        foreach(lst, foreach_test_func)
        self.assertEqual(lst.data, [None]) 
    def test_foreach_not_empty(self):
        lst = List([1, 2, 3, None], 3, 4)
        foreach(lst, foreach_test_func)
        self.assertEqual(lst, List([1, 2, 3, None], 3, 4))

    def test_sort(self):
        self.assertEqual(sort(List([Song('3', '3', '3', '3'), Song('2', '2', '2', '2'), Song('4', '4', '4', '4'), Song('1', '1', '1', '1')], 4, 4), less_than), List([Song('1', '1', '1', '1'), Song('2', '2', '2', '2'), Song('3', '3', '3', '3'), Song('4', '4', '4', '4')], 4, 4))

if __name__ == '__main__':
    unittest.main()
