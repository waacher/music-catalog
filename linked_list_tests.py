import unittest
from linked_list import *

# function to test foreach
# increments the inputted value by one
def foreach_test_func(x):
    return x + 1

# function to test sort
# determines if the first value is smaller than the second
def less_than(x, y):
    if x < y:
        return True
    return False

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

    def test_eq_pair(self):
        self.assertEqual(Pair(4, Pair('asdf', None)), Pair(4, Pair('asdf', None)))
    def test_repr_pair(self):
        self.assertEqual(repr(Pair(4, Pair('asdf', None))), "Pair({!r}, {!r})".format(4, Pair('asdf', None)))

    def test_empty_list(self):
        self.assertEqual(empty_list(), None)
    def test_add_none_error(self):
        self.assertRaises(IndexError, add, None, 3, 'test')
    def test_add_neg_index(self):
        self.assertRaises(IndexError, add, Pair(4, None), -16, 'aye')
    def test_add_empty(self):
        self.assertEqual(add(None, 0, 'test'), Pair('test', None))
    def test_add_mid(self):
        self.assertEqual(add(Pair(3, Pair('qwer', Pair(15, None))), 1, "test"), Pair(3, Pair('test', Pair('qwer', Pair(15, None)))))
    def test_add_invalid(self):
        self.assertRaises(IndexError, add, Pair(3, Pair('asdf', None)), 5, 'something')
    def test_length_empty(self):
        self.assertEqual(length(None), 0) 
    def test_length_small(self):
        self.assertEqual(length(Pair(3, Pair('qwer', Pair(15, None)))), 3)    
    def test_get_empty(self):
        self.assertRaises(IndexError, get, None, 3)
    def test_get_small(self):
        self.assertEqual(get(Pair(3, Pair('qwer', Pair(15, None))), 1), 'qwer')
    def test_set_empty(self):
        self.assertRaises(IndexError, set, None, 1, 2)
    def test_set_valid(self):
        self.assertEqual(set(Pair(3, Pair('qwer', Pair(15, None))), 2, 'test'), Pair(3, Pair('qwer', Pair('test', None))))
    def test_set_invalid(self):
        self.assertRaises(IndexError, set, Pair(4, Pair('zxcv', None)), 7, 'hey') 
    def test_remove_helper(self):
        self.assertEqual(remove_helper(Pair(2, Pair(4, Pair(3, None))), 1), Pair(2, Pair(3, None)))
    def test_remove_helper_error(self):
        self.assertRaises(IndexError, remove_helper, Pair(2, None), 5) 
    def test_remove_empty_over(self):
        self.assertRaises(IndexError, remove, None, 3)
    def test_remove_empty_zero(self):
        self.assertRaises(IndexError, remove, None, 0)
    def test_remove_empty_negative(self):
        self.assertRaises(IndexError, remove, None, -1)
    def test_remove_over(self):
        self.assertRaises(IndexError, remove, Pair(1, Pair(2, None)), 2)
    def test_remove_mid_valid(self):
        self.assertEqual(remove(Pair(1, Pair('asdfg', Pair(26, Pair('nvweqw', None)))), 1), ('asdfg', Pair(1, Pair(26, Pair('nvweqw', None)))))
    def test_remove_end_valid(self):
        self.assertEqual(remove(Pair('zxcv', Pair(745, Pair(27, None))), 2), (27, Pair('zxcv', Pair(745, None))))
    def test_remove_begin_valid(self):
        self.assertEqual(remove(Pair(1, Pair(2, Pair(3, None))), 0), (1, Pair(2, Pair(3, None))))

    def test_repr_song(self):
        self.assertEqual(repr(Song('title', 'artist', 'album', 'num')), "Song({!r}, {!r}, {!r}, {!r})".format('title', 'artist', 'album', 'num'))
    def test_search_mid(self):
        self.assertEqual(search(Pair(Song('1', '2', '3', 4), Pair(Song('1', '1', '1', 1), Pair(Song('2', '3', '4', 7), None))), 1), Song('1', '1', '1', 1))
    def test_search_beg(self):
        self.assertEqual(search(Pair(Song('1', '2', '3', 4), Pair(Song('1', '1', '1', 1), Pair(Song('2', '3', '4', 7), None))), 4), Song('1', '2', '3', 4))

    def test_foreach_empty(self):
        lst = empty_list()
        foreach(lst, foreach_test_func)
        self.assertEqual(lst, None)
    def test_foreach_not_empty(self):
        lst = Pair(1, Pair(2, Pair(3, None)))
        foreach(lst, foreach_test_func)    
        self.assertEqual(lst, Pair(1, Pair(2, Pair(3, None))))

    def test_sort(self):
        self.assertEqual(sort(Pair(3, Pair(1, Pair(5, Pair(4, Pair(2, None))))), less_than), Pair(1, Pair(2, Pair(3, Pair(4, Pair(5, None))))))

if __name__ == '__main__':
    unittest.main()
