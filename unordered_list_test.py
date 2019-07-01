# A program to test the function of the unordered list class

import unittest
from unordered_list import UnorderedList


class ULTestCase(unittest.TestCase):
    """Ensures proper functioning of unordered list methods"""

    def test_UL_empty(self):
        """Ensures Unordered List returns correct boolean re: existance of contents"""
        empty_list = UnorderedList()
        self.assertEqual(True, empty_list.isEmpty())

    def test_UL_add(self):
        """Ensures that add & search methods function properly"""
        add_list = UnorderedList()
        add_list.add(5)
        self.assertEqual(True, add_list.search(5))

    def test_UL_remove(self):
        """Ensures that remove method funcitons properly"""
        remove_list = UnorderedList()
        for number in range(0, 9):
            remove_list.add(number)
        self.assertEqual(False, remove_list.search(9))

    def test_UL_length(self):
        """Ensures that length method functions properly"""
        length_list = UnorderedList()
        for number in range(0, 5):
            length_list.add(1)

        self.assertEqual(5, length_list.length())

    def test_UL_pop(self):
        """Ensures that pop function works both with and without argument"""
        pop_list = UnorderedList()
        for number in range(1, 10):
            pop_list.add(number)
        self.assertEqual(1, pop_list.pop())
        self.assertEqual(5, pop_list.pop(3))

    def test_UL_index(self):
        """Ensures that index method works properly"""
        index_list = UnorderedList()
        for number in range(1, 10):
            index_list.add(number)
        self.assertEqual(3, index_list.index(4))

    def test_UL_append(self):
        """Ensures that append and pop methods function properly"""
        append_list = UnorderedList()
        for number in range(1, 10):
            append_list.add(number)
        append_list.append(11)
        self.assertEqual(11, append_list.pop())

    def test_UL_insert(self):
        """Ensures that the insert method functions properly"""
        insert_list = UnorderedList()
        for number in range(1, 10):
            insert_list.add(number)
        insert_list.insert(12, 5)
        self.assertEqual(12, insert_list.pop(6))

    def test_UL_remove_notfound(self):
        """Ensures that the remove function can handle the situation in which a user requests to
        remove a value that is not in the list"""
        rm_notfound_list = UnorderedList()
        for number in range(0, 9):
            rm_notfound_list.add(number)
        self.assertEqual(False, rm_notfound_list.remove(15))


unittest.main()
