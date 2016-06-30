# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import unittest

from word_counter import solution

__all__ = [
    'TestWordCounter',
]


class TestWordCounter(unittest.TestCase):

    def test_empty_string_returns_empty_tuple(self):
        self.assertEqual(solution(''), ([], []))

    def test_string_with_one_word_returns_same_word_as_least_and_most_common(self):
        self.assertEqual(solution('a'), ([('a', 1)], [('a', 1)]))

    def test_string_with_one_word_returns_same_word_as_least_and_most_common_2(self):
        self.assertEqual(solution('b'), ([('b', 1)], [('b', 1)]))

    def test_string_with_one_word_returns_same_word_as_least_and_most_common_3(self):
        self.assertEqual(solution('c'), ([('c', 1)], [('c', 1)]))

    def test_string_with_one_word_returns_same_word_as_least_and_most_common_4(self):
        self.assertEqual(solution('aa'), ([('aa', 1)], [('aa', 1)]))

    def test_string_with_two_equal_words_returns_same_word_as_least_and_most_common(self):
        self.assertEqual(solution('a a'), ([('a', 2)], [('a', 2)]))

    def test_string_with_three_equal_words_returns_same_word_as_least_and_most_common(self):
        self.assertEqual(solution('a a a'), ([('a', 3)], [('a', 3)]))

    def test_string_with_two_differents_words_returns_two_different_words_with_same_count(self):
        self.assertEqual(solution('a b'), ([('a', 1), ('b', 1)], [('a', 1), ('b', 1)]))

    def test_string_with_three_words_one_different_and_two_equal_returns_the_correct_list(self):
        self.assertEqual(solution('a a b'), ([('b', 1), ('a', 2)], [('a', 2), ('b', 1)]))

    def test_string_with_four_words_two_equal_returns_the_correct_list(self):
        self.assertEqual(solution('a a b b'), ([('a', 2), ('b', 2)], [('a', 2), ('b', 2)]))


if __name__ == '__main__':
    unittest.main()
