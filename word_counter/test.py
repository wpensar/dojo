# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import unittest

from airplane import solution

__all__ = [
    'TestWordCounter',
]


class TestWordCounter(unittest.TestCase):

    def test_fail(self):
        self.assertEqual(solution(''), tuple())


if __name__ == '__main__':
    unittest.main()
